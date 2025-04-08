from injector import inject
from pydantic import BaseModel, field_serializer

from vectorizer_api.domain.factory.vectorizer_factory import (
    VectorizerFactoryInterface,
    VectorizerType,
)
from vectorizer_api.domain.service.vectorizer import VectorizeInput
from vectorizer_api.utils.image import base642pil


class VectorizeRequest(BaseModel):
    vectorizer_type: VectorizerType
    texts: list[str] | None = None
    images: list[str] | None = None

    @field_serializer("vectorizer_type")
    def serialize_vectorizer_type(self, vectorizer_type: VectorizerType) -> str:
        return vectorizer_type.value


class VectorizeResponse(BaseModel):
    vectors: list[list[float]]


class VectorizerUserInterface:
    @inject
    def __init__(self, vectorizer_factory: VectorizerFactoryInterface):
        self.vectorizer_factory = vectorizer_factory

    def vectorize(self, vectorize_request: VectorizeRequest) -> VectorizeResponse:
        vectorizer = self.vectorizer_factory.create(vectorize_request.vectorizer_type)
        vectorize_input = VectorizeInput(
            texts=vectorize_request.texts,
            images=[base642pil(image) for image in vectorize_request.images]
            if vectorize_request.images
            else None,
        )
        vectorize_output = vectorizer.vectorize(vectorize_input)
        return VectorizeResponse(vectors=vectorize_output.vectors)
