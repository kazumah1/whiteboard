from pydantic import BaseModel
from models.whiteboard_object import WhiteboardObject
from typing import Dict, List

class WhiteboardState(BaseModel):
    current_objects: Dict[str, WhiteboardObject] # id : object
    traversal_steps: List[str] # DLL step IDs that led to state
    concept_tags: List[str] # optional tags (e.g. "dot product", "row_column")
    spatial_map: Dict[str, str] | None # semantic layout (e.g. "top_left" : "5x = 10")
    recent_command_ids: List[str] # last N command_ids