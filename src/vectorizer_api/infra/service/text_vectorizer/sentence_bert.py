import torch
from transformers.models.auto.modeling_auto import AutoModel
from transformers.models.auto.tokenization_auto import AutoTokenizer

from vectorizer_api.domain.model.vectorize import VectorizeInput, VectorizeOutput
from vectorizer_api.domain.service.vectorizer import Vectorizer
from vectorizer_api.settings import get_settings
from vectorizer_api.utils.logger import get_logger

logger = get_logger(__name__)

settings = get_settings()


class SentenceBert(Vectorizer):
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            settings.sentence_bert_model_name
        )
        self.model = AutoModel.from_pretrained(settings.sentence_bert_model_name)
        self.model.eval()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)

    def _mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[
            0
        ]  # First element of model_output contains all token embeddings
        input_mask_expanded = (
            attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        )
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(
            input_mask_expanded.sum(1), min=1e-9
        )

    @torch.no_grad()
    def encode(self, sentences: list[str], batch_size: int) -> list[list[float]]:
        all_embeddings = []
        iterator = range(0, len(sentences), batch_size)
        for batch_idx in iterator:
            batch = sentences[batch_idx : batch_idx + batch_size]

            encoded_input = self.tokenizer.batch_encode_plus(
                batch, padding="longest", truncation=True, return_tensors="pt"
            ).to(self.device)
            model_output = self.model(**encoded_input)
            sentence_embeddings = self._mean_pooling(
                model_output, encoded_input["attention_mask"]
            ).to("cpu")

            all_embeddings.extend(sentence_embeddings)

        return torch.stack(all_embeddings).tolist()

    def vectorize(self, vectorize_input: VectorizeInput) -> VectorizeOutput:
        if vectorize_input.texts is None:
            error_msg = "texts is empty"
            logger.error(error_msg)
            raise ValueError(error_msg)

        vectors = self.encode(
            vectorize_input.texts, batch_size=settings.sentence_bert_batch_size
        )
        return VectorizeOutput(vectors=vectors)
