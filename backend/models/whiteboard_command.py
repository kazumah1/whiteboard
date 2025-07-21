from pydantic import BaseModel
from typing import Optional, Dict, Any
from models.whiteboard_object import ExcalidrawElement

class WhiteboardCommand(BaseModel):
    element: ExcalidrawElement  # The Excalidraw element to add or modify
    delay: Optional[float] = 0.0  # When to start (seconds into playback)
    duration: Optional[float] = None  # For animations
    step_id: Optional[str] = None  # Associated DLL step id
    narration_tag: Optional[str] = None  # Optional prompt hint for narration generation
    meta: Optional[Dict[str, Any]] = None  # Any other info