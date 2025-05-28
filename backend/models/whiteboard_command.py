from pydantic import BaseModel
from typing import Literal, Dict, Union

class WhiteboardCommand(BaseModel):
    id: str  # Unique command ID (used for undo/redo targeting)
    type: Literal["draw", "erase", "move", "highlight", "animate"]
    shape: Literal["text", "line", "arrow", "circle", "rect"]
    props: Dict[str, Union[str, int, float]]  # Raw Konva-like props: x, y, points, text, fill, etc.
    target_id: str | None = None  # For erasing/moving/highlighting
    delay: float | None = 0.0  # When to start (seconds into playback)
    duration: float | None = None  # For animations
    step_id: str | None = None  # Associated DLL step id
    narration_tag: str | None = None  # Optional prompt hint for narration generation
    meta: Dict[str, str] | None = None  # Any other info: "semantic_tag", "hint", etc.