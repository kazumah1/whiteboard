from pydantic import BaseModel
from models.step_node import StepDLLNode
from models.narration_event import NarrationEvent
from typing import Dict, List, Optional
from models.command_group import CommandGroup

class LessonNode(BaseModel): # a node in the lesson DAG
    id: str # unique identifier for the lesson node
    steps_DLL_root: StepDLLNode = StepDLLNode(
        id="default_root",
        prev=None,
        next=None,
        commands=[],
        narrate=False,
        narration_trigger_id=None
    )
    current_step: StepDLLNode = steps_DLL_root # current step in the DLL
    next: Optional['LessonNode'] = None # pointer to next lesson node
    branches: Dict[str, 'LessonNode'] = {} # map of branches if any
    is_completed: bool = False # whether the lesson node is completed
    is_terminal: bool = False # whether the lesson node is terminal
    narration_log: List[NarrationEvent] = [] # list of narration events that have been triggered for this lesson node
    narration_map: Dict[str, NarrationEvent] = {} # narration id : narration event

    def get_current_step(self) -> StepDLLNode:
        return self.current_step
    
    def get_current_command_group(self) -> CommandGroup:
        return self.current_step.commands[self.current_step.current_command_group_index]

LessonNode.update_forward_refs()