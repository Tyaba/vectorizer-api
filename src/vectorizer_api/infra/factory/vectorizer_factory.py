from vectorizer_api.domain.factory.vectorizer_factory import (
    VectorizerFactoryInterface,
    VectorizerType,
)
from vectorizer_api.domain.service.vectorizer import Vectorizer
from vectorizer_api.infra.service.image_vectorizer.dreamsim import DreamSim
from vectorizer_api.infra.service.text_vectorizer.sentence_bert import SentenceBert


class VectorizerFactory(VectorizerFactoryInterface):
    def create(self, vectorizer_type: VectorizerType) -> Vectorizer:
        match vectorizer_type:
            case VectorizerType.DREAMSIM:
                return DreamSim()
            case VectorizerType.SENTENCE_BERT:
                return SentenceBert()
            case _:
                error_msg = f"Invalid vectorizer type: {vectorizer_type}"
                raise ValueError(error_msg)
