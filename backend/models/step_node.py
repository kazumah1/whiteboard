from pydantic import BaseModel
from typing import List, Optional
from models.command_group import CommandGroup

class StepDLLNode(BaseModel): # a node in the script DLL
    id: str # unique id for the step
    prev: Optional['StepDLLNode'] = None # pointer to previous node in DLL
    next: Optional['StepDLLNode'] = None # pointer to next node in DLL
    commands: List[CommandGroup] = [] # list of command groups to be executed. Typically one command group per step.
    current_command_group_index: int = 0 # index of the current command group to be executed
    narrate: bool = False # whether narration should be triggered when the step is reached
    narration_trigger_id: str | None = None # the id of the narration to be triggered when the step is reached

StepDLLNode.update_forward_refs()