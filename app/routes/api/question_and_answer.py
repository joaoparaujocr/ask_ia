from fastapi import APIRouter
from schemas.question_and_answer_schema import QuestionRequest, QuestionResponse
from services.assistant_service import AssistantService

router = APIRouter(prefix="/api")

service = AssistantService()

@router.post("/question-and-answer", response_model=QuestionResponse)
def question_and_answer(payload: QuestionRequest):
    response = service.answer(payload.question)
    return QuestionResponse(response=response)