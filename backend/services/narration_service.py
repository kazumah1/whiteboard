from models.narration_event import NarrationEvent
from models.lesson_node import LessonNode
from models.traversal_state import TraversalState
from models.step_node import StepDLLNode
from models.lesson_plan import LessonPlan
from typing import List
from services.script_generator_service import ScriptGeneratorService

# handles generating narration scripts and handling clarification requests (chatting with the LLM)
# specifically for the narration of the lesson 
# TODO: add frontend integration
# TODO: add LLM API calls
# TODO: add RAG operations

class NarrationService:
    def __init__(self, script_generator: ScriptGeneratorService, lesson_plan: LessonPlan):
        self.script_generator = script_generator
        self.lesson_plan = lesson_plan

    async def generate_narration(
        self,
        step_id: str,
        context: TraversalState
    ) -> str:
        # Get visual elements from commands
        visual_elements = self._get_visual_elements(step_id)
        # Get previous context from traversal history
        previous_context = self._get_previous_context(context)
        # Generate the narration script using the script generator
        narration = await self.script_generator.generate_narration_script(
            topic="Pythagorean Theorem",  # This could be dynamic based on the lesson
            step_description=step_id,
            previous_context=previous_context,
            visual_elements=visual_elements
        )
        return narration

    def _get_visual_elements(self, step_id: str) -> str:
        """Extract visual elements from step commands using ID-based lookups"""
        elements = []
        step = self.lesson_plan.steps[step_id]
        for group_id in step.command_group_ids:
            group = self.lesson_plan.command_groups[group_id]
            for command_id in group.command_ids:
                command = self.lesson_plan.commands[command_id]
                el = self.lesson_plan.elements[command.element_id]
                if el.type == "text":
                    elements.append(f"Text: {el.text}")
                elif el.type in ["line", "arrow"]:
                    elements.append(f"{el.type.capitalize()}: {getattr(el, 'points', '')}")
        return "\n".join(elements)

    def _get_previous_context(self, context: TraversalState) -> str:
        """Get context from previous steps"""
        # TODO: Implement context retrieval from traversal history
        return "Previous steps context"

    async def handle_clarification(
        self,
        question: str,
        narration_history: List[NarrationEvent],
        context: TraversalState,
        concept: LessonNode
    ) -> str:
        # Format the context from narration history
        context_str = self._format_narration_history(narration_history)
        # Use the script generator to handle the clarification
        return await self.script_generator.handle_clarification(
            question=question,
            context=context_str
        )

    def _format_narration_history(self, history: List[NarrationEvent]) -> str:
        """Format narration history into a context string"""
        return "\n".join([f"Step {event.start_step}: {event.utterance}" for event in history])