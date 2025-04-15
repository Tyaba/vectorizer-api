from abc import ABC, abstractmethod

from vectorizer_api.domain.model.vectorize import VectorizerType
from vectorizer_api.domain.service.vectorizer import Vectorizer


class VectorizerFactoryInterface(ABC):
    @abstractmethod
    def create(self, vectorizer_type: VectorizerType) -> Vectorizer:
        pass
