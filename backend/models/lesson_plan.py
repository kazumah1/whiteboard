from pydantic import BaseModel
from models.lesson_node import LessonNode
from models.traversal_history import TraversalHistory
from models.step_node import StepDLLNode
from models.command_group import CommandGroup
from typing import Dict

class LessonPlan(BaseModel):
    id: str
    title: str
    lesson_root: LessonNode
    nodes: Dict[str, LessonNode]
    traversal_history: TraversalHistory