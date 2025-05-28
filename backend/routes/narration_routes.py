from fastapi import APIRouter, Depends
from services.narration_service import NarrationService
from models.narration_event import NarrationEvent
from models.traversal_state import TraversalState
from models.lesson_node import LessonNode
from models.step_node import StepDLLNode
from typing import List

router = APIRouter()

@router.post("/{lesson_id}/ask")
async def ask_question(
    lesson_id: str,
    question: str,
    narration_history: List[NarrationEvent],
    context: TraversalState,
    concept: LessonNode,
    narration_service: NarrationService = Depends()
):
    return await narration_service.handle_clarification(question, narration_history, context, concept)

@router.post("/{lesson_id}/narrate")
async def narrate_step(
    lesson_id: str,
    step: StepDLLNode,
    narration_history: List[NarrationEvent],
    context: TraversalState,
    concept: LessonNode,
    narration_service: NarrationService = Depends()
):
    return await narration_service.generate_narration(step, narration_history, context, concept)