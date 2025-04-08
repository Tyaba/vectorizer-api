from abc import ABC, abstractmethod
from enum import Enum

from src.vectorizer_api.domain.service.vectorizer import Vectorizer


class VectorizerType(Enum):
    IMAGE = "image"


class VectorizerFactoryInterface(ABC):
    @abstractmethod
    def create(self, vectorizer_type: VectorizerType) -> Vectorizer:
        pass
