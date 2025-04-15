from PIL import Image
from pydantic import BaseModel, ConfigDict, field_serializer, model_validator
from typing import Self

from enum import Enum

from vectorizer_api.utils.logger import get_logger
logger = get_logger(__name__)

class VectorizerType(Enum):
    DREAMSIM = "dreamsim"
    SENTENCE_BERT = "sentence_bert"

class VectorizeInput(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    texts: list[str] | None = None
    images: list[Image.Image] | None = None

    @model_validator(mode="after")
    def validate_input(self) -> Self:
        if self.texts is None and self.images is None:
            error_msg = "texts and images cannot be None at the same time"
            logger.error(error_msg)
            raise ValueError(error_msg)
        return self

class VectorizeOutput(BaseModel):
    vectors: list[list[float]]


class VectorizeRequest(BaseModel):
    vectorizer_type: VectorizerType
    texts: list[str] | None = None
    images: list[str] | None = None

    @field_serializer("vectorizer_type")
    def serialize_vectorizer_type(self, vectorizer_type: VectorizerType) -> str:
        return vectorizer_type.value

    @model_validator(mode="after")
    def validate_input_type(self) -> Self:
        text_vectorizers = {VectorizerType.SENTENCE_BERT}
        image_vectorizers = {VectorizerType.DREAMSIM}
        if self.images is not None and self.vectorizer_type in text_vectorizers:
            error_msg = f"images cannot be vectorized by {self.vectorizer_type}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        if self.texts is not None and self.vectorizer_type in image_vectorizers:
            error_msg = f"texts cannot be vectorized by {self.vectorizer_type}"
            logger.error(error_msg)
            raise ValueError(error_msg)
        return self


class VectorizeResponse(BaseModel):
    vectors: list[list[float]]

