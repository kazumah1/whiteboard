from pydantic import BaseModel
from typing import List, Optional
from models.traversal_state import TraversalState

class TraversalHistory(BaseModel):
    history: Optional[List[TraversalState]] = [TraversalState(
        current_node_id="root",
        current_step_id="root",
        narration_event_id="root"
    )]

    def current(self) -> TraversalState:
        return self.history[-1]
    
    def push(self, state: TraversalState) -> None:
        self.history.append(state)

    def back(self, steps: int = 1) -> TraversalState:
        return self.history[-steps]
    
    def undo(self) -> TraversalState:
        if len(self.history) != 1:
            self.history.pop()
            return self.history[-1]
        return None
    
