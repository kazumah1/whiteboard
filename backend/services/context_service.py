from typing import Dict, Any
from models.traversal_state import TraversalState
from models.step_node import StepDLLNode
from models.lesson_node import LessonNode
from services.traversal_service import TraversalService
from services.rag_service import RAGService

class ContextService:
    def __init__(self, traversal_service: TraversalService, rag_service: RAGService):
        self.traversal_service = traversal_service
        self.rag_service = rag_service

    async def get_step_context(self, step_id: str) -> Dict[str, Any]:
        """
        Gather all relevant context for a step
        
        Args:
            step_id: The ID of the step to get context for
            
        Returns:
            Dictionary containing all relevant context
        """
        # Get the current state
        state = self.traversal_service.get_current_state()
        
        # Get the current step
        step = self._get_step_by_id(step_id, state)
        
        # Get the current lesson node
        lesson_node = self._get_lesson_node_by_step(step_id, state)
        
        # Get visual elements from the step
        visual_elements = self._get_visual_elements(step)
        
        # Get previous context from traversal history
        previous_context = self._get_previous_context(state)
        
        # Get RAG context if needed
        rag_context = await self.rag_service.get_relevant_context(step_id)
        
        return {
            "step_description": step.id,
            "topic": lesson_node.id,  # or some other topic identifier
            "previous_context": previous_context,
            "board_state": self._get_board_state(step),
            "new_visual_elements": visual_elements,
            "rag_context": rag_context
        }

    def _get_step_by_id(self, step_id: str, state: TraversalState) -> StepDLLNode:
        """Get a step node by its ID"""
        # TODO: Implement step lookup
        pass

    def _get_lesson_node_by_step(self, step_id: str, state: TraversalState) -> LessonNode:
        """Get the lesson node containing a step"""
        # TODO: Implement lesson node lookup
        pass

    def _get_visual_elements(self, step: StepDLLNode) -> str:
        """Extract visual elements from step commands"""
        elements = []
        for command_group in step.commands:
            for command in command_group.commands:
                if command.shape == "text":
                    elements.append(f"Text: {command.props['text']}")
                elif command.shape in ["line", "arrow"]:
                    elements.append(f"{command.shape.capitalize()}: {command.props.get('points', '')}")
        return "\n".join(elements)

    def _get_previous_context(self, state: TraversalState) -> str:
        """Get context from previous steps"""
        # TODO: Implement context retrieval from traversal history
        return "Previous steps context"

    def _get_board_state(self, step: StepDLLNode) -> str:
        """Get the current state of the whiteboard"""
        # TODO: Implement board state retrieval
        return "Current board state" 