from pydantic import BaseModel, Field
from typing import Optional, List, Literal, Dict, Any

class ExcalidrawElement(BaseModel):
    id: str
    type: Literal[
        "rectangle", "ellipse", "diamond", "text", "arrow", "line", "frame"
    ]
    x: float
    y: float
    width: Optional[float] = None
    height: Optional[float] = None
    text: Optional[str] = None  # for text elements
    points: Optional[List[List[float]]] = None  # for lines/arrows
    strokeColor: Optional[str] = None
    backgroundColor: Optional[str] = None
    strokeWidth: Optional[float] = None
    strokeStyle: Optional[Literal["solid", "dashed", "dotted"]] = None
    fillStyle: Optional[Literal["solid", "hachure", "cross-hatch"]] = None
    roughness: Optional[float] = None
    opacity: Optional[float] = None
    angle: Optional[float] = None
    groupIds: Optional[List[str]] = None
    boundElements: Optional[List[str]] = None
    locked: Optional[bool] = None
    link: Optional[str] = None
    seed: Optional[int] = None
    version: Optional[int] = None
    versionNonce: Optional[int] = None
    isDeleted: Optional[bool] = None
    label: Optional[Dict[str, Any]] = None  # for text containers, arrows
    start: Optional[Dict[str, Any]] = None  # for arrow bindings
    end: Optional[Dict[str, Any]] = None    # for arrow bindings
    children: Optional[List[str]] = None    # for frames
    name: Optional[str] = None              # for frames
    
    # Text-specific properties
    fontSize: Optional[int] = None
    fontFamily: Optional[int] = None
    textAlign: Optional[str] = None
    verticalAlign: Optional[str] = None
    containerId: Optional[str] = None
    originalText: Optional[str] = None
    lineHeight: Optional[float] = None
    baseline: Optional[float] = None
    
    # Line-specific properties
    startArrowhead: Optional[str] = None
    endArrowhead: Optional[str] = None
    startBinding: Optional[Dict[str, Any]] = None
    endBinding: Optional[Dict[str, Any]] = None
    
    # Additional properties that might be needed
    strokeSharpness: Optional[str] = None
    commentCount: Optional[int] = None
    updated: Optional[int] = None