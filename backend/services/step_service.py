from models.step_node import StepDLLNode
from models.command_group import CommandGroup
from models.whiteboard_command import WhiteboardCommand
from models.traversal_state import TraversalState
from models.whiteboard_object import ExcalidrawElement
from typing import Optional, List

class StepService:
    """
    Handles traversal and execution of steps (DLL) within a LessonNode.
    """
    
    def next_step(self, current_step: StepDLLNode) -> Optional[StepDLLNode]:
        """Move to the next step in the DLL, if available."""
        return current_step.next

    def prev_step(self, current_step: StepDLLNode) -> Optional[StepDLLNode]:
        """Move to the previous step in the DLL, if available."""
        return current_step.prev

    def reset_step(self, step: StepDLLNode) -> None:
        """Reset the current command group index for all command groups in this step."""
        for group in step.commands:
            group.reset()

    def get_current_command_group(self, step: StepDLLNode) -> CommandGroup:
        """Get the current command group for this step."""
        return step.commands[step.current_command_group_index]

    def execute_step(self, step: StepDLLNode, state: TraversalState) -> List[ExcalidrawElement]:
        """
        Execute all commands in all command groups for the given step.
        Returns a flat list of ExcalidrawElement objects to be rendered for this step.
        """
        try:
            print(f"Executing step: {step.id}")
            print(f"Step has {len(step.commands)} command groups")
            
            elements: List[ExcalidrawElement] = []
            for i, group in enumerate(step.commands):
                print(f"Processing command group {i}: {group.id}")
                print(f"Group has {len(group.commands)} commands")
                
                for j, command in enumerate(group.commands):
                    print(f"Processing command {j}: {command.element.id}")
                    elements.append(command.element)
            
            print(f"Returning {len(elements)} elements")
            return elements
        except Exception as e:
            print(f"Error in execute_step: {e}")
            import traceback
            traceback.print_exc()
            raise