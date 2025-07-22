from pydantic import BaseModel
from typing import List, Optional

class StepDLLNode(BaseModel):
    id: str
    prev_id: Optional[str] = None
    next_id: Optional[str] = None
    command_group_ids: List[str] = []  # List of CommandGroup IDs
    current_command_group_index: int = 0
    narrate: bool = False
    narration_trigger_id: Optional[str] = None

StepDLLNode.model_rebuild()