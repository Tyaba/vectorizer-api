from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sentence_bert_model_name: str = Field(
        default="sonoisa/sentence-bert-base-ja-mean-tokens-v2",
        description="sentence-bertのモデル名",
    )
    sentence_bert_batch_size: int = Field(
        default=32,
        description="sentence-bertのバッチサイズ",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
