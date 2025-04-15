from pydantic import BaseModel, field_serializer

from vectorizer_api.domain.factory.vectorizer_factory import VectorizerType


class VectorizeRequest(BaseModel):
    vectorizer_type: VectorizerType
    texts: list[str] | None = None
    images: list[str] | None = None

    @field_serializer("vectorizer_type")
    def serialize_vectorizer_type(self, vectorizer_type: VectorizerType) -> str:
        return vectorizer_type.value


class VectorizeResponse(BaseModel):
    vectors: list[list[float]]

