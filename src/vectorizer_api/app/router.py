from functools import partial

from fastapi import APIRouter, Depends

from vectorizer_api.di import resolve
from vectorizer_api.usecase.ui.vectorizer import (
    VectorizeRequest,
    VectorizeResponse,
    VectorizerUserInterface,
)

router = APIRouter()


@router.post("/vectorize")
def vectorize(
    request: VectorizeRequest,
    vectorizer_user_interface: VectorizerUserInterface = Depends(
        partial(resolve, VectorizerUserInterface)
    ),
) -> VectorizeResponse:
    return vectorizer_user_interface.vectorize(request)
