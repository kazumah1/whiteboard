from pydantic import BaseModel
from typing import List
from models.whiteboard_object import ExcalidrawElement

class WhiteboardState(BaseModel):
    elements: List[ExcalidrawElement]  # The current list of Excalidraw elements on the board