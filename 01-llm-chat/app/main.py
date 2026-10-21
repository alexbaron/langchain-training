from fastapi import FastAPI

from app.models import (
    QuestionRequest,
    QuestionResponse
)

app = FastAPI()

@app.post(
    "/ask",
    response_model=QuestionResponse
)
def ask(data: QuestionRequest):

    return QuestionResponse(
        answer=f"Question reçue : {data.question}"
    )