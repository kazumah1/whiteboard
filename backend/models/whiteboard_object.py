from pydantic import BaseModel
from typing import Literal, Dict, List, Union

class WhiteboardObject(BaseModel):
    id: str
    shape: Literal["text", "line", "arrow", "circle", "rect"]
    props: Dict[str, Union[str, int, float]]
    semantic_tags: List[str] | None = None