from pydantic import BaseModel
from typing import List

class CommandGroup(BaseModel):
    id: str
    command_ids: List[str]  # List of WhiteboardCommand IDs
    current_command_index: int
    step_id: str