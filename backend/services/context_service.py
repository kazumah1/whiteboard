from typing import Dict, Any
from models.traversal_state import TraversalState
from models.step_node import StepDLLNode
from models.lesson_node import LessonNode
from services.traversal_service import TraversalService
# from services.rag_service import RAGService

class ContextService:
    def __init__(self, traversal_service: TraversalService):
        self.traversal_service = traversal_service
        # self.rag_service = rag_service

    async def get_step_context(self, step_id: str) -> Dict[str, Any]:
        """
        Gather all relevant context for a step
        """
        state = self.traversal_service.get_current_state()
        step = self._get_step_by_id(step_id, state)
        lesson_node = self._get_lesson_node_by_step(step_id, state)
        visual_elements = self._get_visual_elements(step)
        previous_context = self._get_previous_context(state)
        # rag_context = await self.rag_service.get_relevant_context(step_id)
        return {
            "step_description": step.id,
            "topic": lesson_node.id,
            "previous_context": previous_context,
            "board_state": self._get_board_state(step, lesson_node),
            "new_visual_elements": visual_elements,
            # "rag_context": rag_context
        }

    def _get_step_by_id(self, step_id: str, state: TraversalState) -> StepDLLNode:
        """
        Look up a StepDLLNode by ID, starting from the current lesson node.
        """
        lesson_node = self._get_lesson_node_by_id(state.current_node_id)
        step = lesson_node.steps_DLL_root
        while step:
            if step.id == step_id:
                return step
            step = step.next
        raise ValueError(f"Step with id {step_id} not found in current lesson node.")

    def _get_lesson_node_by_step(self, step_id: str, state: TraversalState) -> LessonNode:
        """
        Find the LessonNode that contains the given step_id.
        """
        # For now, just use the current node from state
        return self._get_lesson_node_by_id(state.current_node_id)

    def _get_lesson_node_by_id(self, node_id: str) -> LessonNode:
        """
        Look up a LessonNode by ID from the lesson plan.
        """
        # Assumes the lesson plan is accessible via traversal_service
        plan = self.traversal_service.lesson_service.plan
        return plan.nodes[node_id]

    def _get_visual_elements(self, step: StepDLLNode) -> str:
        elements = []
        for command_group in step.commands:
            for command in command_group.commands:
                if command.shape == "text":
                    elements.append(f"Text: {command.props['text']}")
                elif command.shape in ["line", "arrow"]:
                    elements.append(f"{command.shape.capitalize()}: {command.props.get('points', '')}")
        return "\n".join(elements)

    def _get_previous_context(self, state: TraversalState) -> str:
        """
        Return a summary of previous steps from traversal history.
        """
        history = self.traversal_service.history.history
        if not history or len(history) < 2:
            return ""
        # Exclude the current state
        prev_states = history[:-1]
        context_lines = []
        for s in prev_states:
            try:
                node = self._get_lesson_node_by_id(s.current_node_id)
                step = self._get_step_by_id(s.current_step_id, s)
                context_lines.append(f"Node: {node.id}, Step: {step.id}")
            except Exception:
                continue
        return "\n".join(context_lines)

    def _get_board_state(self, step: StepDLLNode, lesson_node: LessonNode) -> str:
        """
        Return a summary of all commands up to the current step in the lesson node.
        """
        commands = []
        s = lesson_node.steps_DLL_root
        while s and s != step:
            for group in s.commands:
                for command in group.commands:
                    commands.append(f"{command.shape}: {command.props}")
            s = s.next
        return "\n".join(commands) 