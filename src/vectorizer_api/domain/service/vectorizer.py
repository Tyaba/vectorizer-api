from abc import ABC, abstractmethod


from vectorizer_api.domain.model.vectorize import VectorizeInput, VectorizeOutput
from vectorizer_api.utils.logger import get_logger

logger = get_logger(__name__)

class Vectorizer(ABC):
    @abstractmethod
    def vectorize(self, vectorize_input: VectorizeInput) -> VectorizeOutput:
        pass
