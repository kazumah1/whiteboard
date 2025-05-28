from pydantic import BaseModel
from typing import List, Optional
from models.traversal_state import TraversalState

class TraversalHistory(BaseModel):
    history: Optional[List[TraversalState]] = []

    def current(self) -> TraversalState:
        return self.history[-1]
    
    def push(self, state: TraversalState) -> None:
        self.history.append(state)

    def back(self, steps: int = 1) -> TraversalState:
        return self.history[-steps]
    
    def undo(self) -> TraversalState:
        return self.history.pop()
    
