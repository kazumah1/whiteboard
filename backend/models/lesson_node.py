from pydantic import BaseModel
from typing import List, Dict, Optional

class LessonNode(BaseModel):
    id: str
    steps_DLL_root_id: str  # ID of the first step in the DLL
    next_id: Optional[str] = None
    branch_ids: List[str] = []  # List of branch node IDs
    is_completed: bool = False
    is_terminal: bool = False
    # ...other fields as needed...

LessonNode.model_rebuild()