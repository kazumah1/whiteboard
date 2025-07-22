from __future__ import annotations
from pydantic import BaseModel
from typing import Dict
from .lesson_node import LessonNode
from .step_node import StepDLLNode
from .command_group import CommandGroup
from .whiteboard_command import WhiteboardCommand
from .whiteboard_object import ExcalidrawElement

class LessonPlan(BaseModel):
    id: str
    title: str
    nodes: Dict[str, "LessonNode"]
    steps: Dict[str, "StepDLLNode"]
    command_groups: Dict[str, "CommandGroup"]
    commands: Dict[str, "WhiteboardCommand"]
    elements: Dict[str, "ExcalidrawElement"]
    # ...other fields as needed...