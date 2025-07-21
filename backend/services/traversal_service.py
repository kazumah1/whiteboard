# for handling DAG traversal, branching, and backtracking over the entire lesson (some DLL traversal)

# should be called by the lesson service or narration service

from models.traversal_state import TraversalState
from models.traversal_history import TraversalHistory
from models.lesson_node import LessonNode
from models.step_node import StepDLLNode
from typing import Optional

class TraversalService:
    """
    Tracks and updates the user's traversal state and history.
    """
    def __init__(self):
        self.history = TraversalHistory(history=[])
        self.current_state: Optional[TraversalState] = None

    def get_current_state(self) -> Optional[TraversalState]:
        """Return the current traversal state."""
        return self.current_state

    def set_current_state(self, state: TraversalState) -> None:
        """Set the current traversal state and push to history."""
        self.current_state = state
        self.history.push(state)

    def back(self, steps: int = 1) -> Optional[TraversalState]:
        """Go back in history by a number of steps."""
        if len(self.history.history) >= steps:
            self.current_state = self.history.back(steps)
            return self.current_state
        return None

    def undo(self) -> Optional[TraversalState]:
        """Undo the last traversal state."""
        if self.history.history:
            self.current_state = self.history.undo()
            return self.current_state
        return None

    def snapshot(self) -> Optional[TraversalState]:
        """Return a snapshot (copy) of the current state."""
        # For now, just return the current state (could deepcopy if needed)
        return self.current_state