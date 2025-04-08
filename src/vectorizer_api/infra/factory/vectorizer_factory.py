from vectorizer_api.domain.factory.vectorizer_factory import (
    VectorizerFactoryInterface,
    VectorizerType,
)
from vectorizer_api.domain.service.vectorizer import Vectorizer
from vectorizer_api.infra.service.image_vectorizer.dreamsim import DreamSim


class VectorizerFactory(VectorizerFactoryInterface):
    def create(self, vectorizer_type: VectorizerType) -> Vectorizer:
        if vectorizer_type == VectorizerType.IMAGE:
            return DreamSim()
        error_msg = f"Invalid vectorizer type: {vectorizer_type}"
        raise ValueError(error_msg)
