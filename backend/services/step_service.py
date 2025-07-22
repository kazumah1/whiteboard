from models.step_node import StepDLLNode
from models.command_group import CommandGroup
from models.whiteboard_command import WhiteboardCommand
from models.traversal_state import TraversalState
from models.whiteboard_object import ExcalidrawElement
from typing import Optional, List
from models.lesson_plan import LessonPlan

class StepService:
    """
    Handles traversal and execution of steps (DLL) within a LessonNode using ID-based lookups.
    """
    
    def next_step(self, lesson_plan: LessonPlan, current_step_id: str) -> Optional[StepDLLNode]:
        current_step = lesson_plan.steps[current_step_id]
        if current_step.next_id:
            return lesson_plan.steps[current_step.next_id]
        return None

    def prev_step(self, lesson_plan: LessonPlan, current_step_id: str) -> Optional[StepDLLNode]:
        current_step = lesson_plan.steps[current_step_id]
        if current_step.prev_id:
            return lesson_plan.steps[current_step.prev_id]
        return None

    def reset_step(self, lesson_plan: LessonPlan, step_id: str) -> None:
        step = lesson_plan.steps[step_id]
        for group_id in step.command_group_ids:
            group = lesson_plan.command_groups[group_id]
            group.current_command_index = 0

    def get_current_command_group(self, lesson_plan: LessonPlan, step_id: str) -> CommandGroup:
        step = lesson_plan.steps[step_id]
        group_id = step.command_group_ids[step.current_command_group_index]
        return lesson_plan.command_groups[group_id]

    def execute_step(self, lesson_plan: LessonPlan, step_id: str, state: TraversalState) -> List[ExcalidrawElement]:
        """
        Execute all commands in all command groups for the given step.
        Returns a flat list of ExcalidrawElement objects to be rendered for this step.
        """
        try:
            step = lesson_plan.steps[step_id]
            elements: List[ExcalidrawElement] = []
            for group_id in step.command_group_ids:
                group = lesson_plan.command_groups[group_id]
                for command_id in group.command_ids:
                    command = lesson_plan.commands[command_id]
                    elements.append(lesson_plan.elements[command.element_id])
            return elements
        except Exception as e:
            print(f"Error in execute_step: {e}")
            import traceback
            traceback.print_exc()
            raise