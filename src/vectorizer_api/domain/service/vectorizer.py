from abc import ABC, abstractmethod
from typing import Self

from PIL import Image
from pydantic import BaseModel, ConfigDict, model_validator

from vectorizer_api.utils.logger import get_logger

logger = get_logger(__name__)


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


class Vectorizer(ABC):
    @abstractmethod
    def vectorize(self, vectorize_input: VectorizeInput) -> VectorizeOutput:
        pass
