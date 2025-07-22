from pydantic import BaseModel
from typing import Optional

class WhiteboardCommand(BaseModel):
    id: str
    element_id: str  # Reference to ExcalidrawElement by ID
    delay: Optional[float] = None
    duration: Optional[float] = None
    step_id: Optional[str] = None
    narration_tag: Optional[str] = None
    meta: Optional[dict] = None