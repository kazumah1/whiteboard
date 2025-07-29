from pydantic import BaseModel
from typing import Optional, List, Literal
# import ..styles.css

# Excalidraw element types (update as Excalidraw adds more)
ExcalidrawElementType = Literal[
    "rectangle",  # Rectangle
    "ellipse",    # Ellipse
    "diamond",    # Diamond
    "text",       # Text
    "arrow",      # Arrow
    "line",       # Line
    "freedraw",   # Freehand/sketch
    "image",      # Image
    "frame",      # Frame
    "selection",  # Selection (rarely used in backend)
    "embeddable", # Embeddable (iframe, etc.)
    "magicframe", # Magic frame (AI)
    # Add more as needed
]

class ExcalidrawElement(BaseModel):
    id: str
    type: ExcalidrawElementType  # See options above
    x: float
    y: float
    width: float
    height: float
    angle: float
    strokeColor: str
    backgroundColor: str
    fillStyle: Optional[str] = None  # "hachure", "cross-hatch", "solid", "zigzag"
    strokeWidth: int
    strokeStyle: Optional[str] = None  # "solid", "dashed", "dotted"
    roughness: int
    opacity: int
    seed: int
    version: int
    versionNonce: int
    isDeleted: bool
    groupIds: List[str]
    updated: int
    locked: bool
    # --- Text-specific ---
    text: Optional[str] = None
    fontSize: Optional[int] = None
    fontFamily: Optional[int] = None
    textAlign: Optional[str] = None  # "left", "center", "right"
    verticalAlign: Optional[str] = None  # "top", "middle", "bottom"
    containerId: Optional[str] = None
    originalText: Optional[str] = None
    autoResize: Optional[bool] = None
    lineHeight: Optional[float] = None
    # --- Line/Arrow/Freedraw-specific ---
    points: Optional[List[List[float]]] = None  # List of [x, y] pairs
    pressures: Optional[List[float]] = None  # For freedraw
    simulatePressure: Optional[bool] = None  # For freedraw
    lastCommittedPoint: Optional[List[float]] = None  # For freedraw/line
    startBinding: Optional[dict] = None  # For arrow/line
    endBinding: Optional[dict] = None    # For arrow/line
    startArrowhead: Optional[str] = None  # For arrow (e.g., "arrow", "dot", ...)
    endArrowhead: Optional[str] = None    # For arrow
    # --- Image-specific ---
    fileId: Optional[str] = None
    status: Optional[str] = None  # "pending", "saved", "error"
    scale: Optional[List[float]] = None  # [x, y] scale
    crop: Optional[dict] = None  # Crop info
    # --- Frame-specific ---
    name: Optional[str] = None
    # --- Embeddable-specific ---
    customData: Optional[dict] = None
    # --- Misc ---
    frameId: Optional[str] = None
    boundElements: Optional[List[dict]] = None
    link: Optional[str] = None
    customData: Optional[dict] = None
    # Add more fields as Excalidraw evolves