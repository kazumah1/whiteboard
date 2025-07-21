from pydantic import BaseModel
from models.step_node import StepDLLNode
from models.lesson_node import LessonNode
from typing import Optional

class TraversalState(BaseModel):
    current_node_id: str
    current_step_id: str
    narration_event_id: Optional[str] = None