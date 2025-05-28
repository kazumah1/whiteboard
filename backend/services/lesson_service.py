from models.lesson_plan import LessonPlan
from models.traversal_history import TraversalHistory
from models.traversal_state import TraversalState
from models.lesson_node import LessonNode
from models.step_node import StepDLLNode
from models.command_group import CommandGroup
from models.whiteboard_command import WhiteboardCommand
from models.narration_event import NarrationEvent
from services.traversal_service import TraversalService
from services.step_service import StepService

# handles creating a lesson and getting positional information (for traversal and frontend)

class LessonService:
    def __init__(self, traversal_service: TraversalService, step_service: StepService):
        self.plan: LessonPlan | None = None
        self.current_node_id: str | None = None
        self.traversal_history: TraversalHistory | None = None
        self.traversal_service = traversal_service
        self.step_service = step_service

    def load_lesson(self, lesson_id: str) -> LessonPlan:
        if True: # eventually check if lesson doesn't exists in db
            self.plan = LessonPlan( # hardcoded for now
                id = lesson_id,
                title = "Pythagorean Theorem",
                lesson_root = LessonNode(
                    id = "pythag intro",
                    steps_DLL_root = StepDLLNode(
                        id = "intro DLL0",
                        prev=None,
                        next=None,
                        commands=[CommandGroup(
                            id = "write Pythagorean Theorem",
                            commands=[WhiteboardCommand(
                                id = "intro command 1",
                                type = "draw",
                                shape = "text",
                                props={"text": "Pythagorean Theorem", "x": 100, "y": 100, "fontSize": 24, "fill": "black"},
                                target_id=None, # no moving or erasing
                                delay=0.0,
                                duration=None, # TODO not animated
                                step_id="intro DLL0",
                                narration_tag=None, # TODO
                                meta=None
                            )],
                            current_command_index=0,
                            step_id="intro DLL0"
                        )],
                        narrate=True, # TODO
                        narration_trigger_id="intro 1"
                    ),
                    branches={}, # TODO
                    is_completed=False,
                    is_terminal=False,
                    narration_log=[],
                    narration_map={"intro 1":NarrationEvent(
                        id = "intro 1",
                        start_step="intro DLL0",
                        end_step="intro DLL0",
                        utterance="The Pythagorean Theorem is a fundamental principle in geometry that relates the lengths of the sides of a right triangle.",
                        sync_map=None, # TODO
                        duration=0.0
                    )},
                    next=LessonNode(
                        id = "pythag triangle",
                        steps_DLL_root = StepDLLNode(
                            id = "pythag triangle DLL0",
                            prev=None,
                            next=None,
                            commands=[CommandGroup(
                                id = "triangle command group 1",
                                commands=[WhiteboardCommand(
                                    id = "triangle command 1",
                                    type = "draw",
                                    shape = "line",
                                    props={"x": 100, "y": 50, "points": "0,0 100,0 100,100 0,100", "stroke": "black", "strokeWidth": 2},
                                    target_id=None,
                                    delay=1.0,
                                    duration=None,
                                    step_id="pythag triangle DLL0",
                                    narration_tag=None, # TODO
                                    meta=None
                                )],
                                current_command_index=0,
                                step_id="pythag triangle DLL0"
                            )],
                            narrate=True,
                            narration_trigger_id="triangle 1"
                        ),
                        branches={}, # TODO
                        is_completed=False,
                        is_terminal=False,
                        narration_log=[],
                        narration_map={"triangle 1":NarrationEvent(
                            id = "triangle 1",
                            start_step="pythag triangle DLL0",
                            end_step="pythag triangle DLL0",
                            utterance="Let's say we have a right triangle.",
                            sync_map=None, # TODO
                            duration=0.0
                        )},
                        next=LessonNode(
                            id = "pythag problem",
                            steps_DLL_root = StepDLLNode(
                                id = "pythag problem DLL0",
                                prev=None,
                                next=None,
                                commands=[CommandGroup(
                                    id = "problem command group 1",
                                    commands=[WhiteboardCommand(
                                        id = "problem command 1",
                                        type = "draw",
                                        shape = "text",
                                        props={"text": "3", "x": 100, "y": 50, "fontSize": 24, "fill": "black"},
                                        step_id="pythag problem DLL0"
                                    ),
                                    WhiteboardCommand(
                                        id = "problem command 2",
                                        type = "draw",
                                        shape = "text",
                                        props={"text": "4", "x": 110, "y": 50, "fontSize": 24, "fill": "black"},
                                        step_id="pythag problem DLL0"
                                    ),
                                    WhiteboardCommand(
                                        id = "problem command 3",
                                        type = "draw",
                                        shape = "text",
                                        props={"text": "c", "x": 120, "y": 50, "fontSize": 24, "fill": "black"},
                                        step_id="pythag problem DLL0"
                                    )],
                                    current_command_index=0,
                                    step_id="pythag problem DLL0"
                                )],
                                narrate=True, # TODO
                                narration_trigger_id="problem 1"
                            ),
                            narration_map={"problem 1":NarrationEvent(
                                id = "problem 1",
                                start_step="pythag problem DLL0",
                                end_step="pythag problem DLL0",
                                utterance="Given a right triangle with sides 3, 4, and c, where c is the hypotenuse, the goal is to find c.",
                                sync_map=None, # TODO
                                duration=0.0
                            )},
                            next=LessonNode(
                                id = "pythag formula",
                                steps_DLL_root = StepDLLNode(
                                    id = "pythag formula DLL0",
                                    prev=None,
                                    next=None,
                                    commands=[CommandGroup(
                                        id = "formula command group 1",
                                        commands=[WhiteboardCommand(
                                            id = "formula command 1",
                                            type = "draw",
                                            shape = "text",
                                            props={"text": "a^2 + b^2 = c^2", "x": 100, "y": 50, "fontSize": 24, "fill": "black"},
                                            step_id="pythag formula DLL0"
                                        )],
                                        current_command_index=0,
                                        step_id="pythag formula DLL0"
                                    )],
                                    narrate=True,
                                    narration_trigger_id="formula 1"
                                ),
                                narration_map={"formula 1":NarrationEvent(
                                    id = "formula 1",
                                    start_step="pythag formula DLL0",
                                    end_step="pythag formula DLL0",
                                    utterance="The equation for the Pythagorean Theorem is a^2 + b^2 = c^2.",
                                    sync_map=None, # TODO
                                    duration=0.0
                                )},
                                next=LessonNode(
                                    id = "pythag solution",
                                    steps_DLL_root = StepDLLNode(
                                        id = "pythag solution DLL0",
                                        prev=None,
                                        next=None,
                                        commands=[CommandGroup(
                                            id = "solution command group 1",
                                            commands=[WhiteboardCommand(
                                                id = "solution command 1",
                                                type = "draw",
                                                shape = "text",
                                                props={"text": "3^2 + 4^2 = c^2", "x": 100, "y": 50, "fontSize": 24, "fill": "black"},
                                                step_id="pythag solution DLL0"
                                            ),
                                            WhiteboardCommand(
                                                id = "solution command 2",
                                                type = "draw",
                                                shape = "text",
                                                props={"text": "9 + 16 = c^2", "x": 100, "y": 50, "fontSize": 24, "fill": "black"},
                                                step_id="pythag solution DLL0"
                                            ),
                                            WhiteboardCommand(
                                                id = "solution command 3",
                                                type = "draw",
                                                shape = "text",
                                                props={"text": "25 = c^2", "x": 100, "y": 50, "fontSize": 24, "fill": "black"},
                                                step_id="pythag solution DLL0"
                                            ),
                                            WhiteboardCommand(
                                                id = "solution command 4",
                                                type = "draw",
                                                shape = "text",
                                                props={"text": "c = 5", "x": 100, "y": 50, "fontSize": 24, "fill": "blue"},
                                                step_id="pythag solution DLL0"
                                            )],
                                            current_command_index=0,
                                            step_id="pythag solution DLL0"
                                        )],
                                        narrate=True,
                                        narration_trigger_id="solution 1"
                                    ),
                                    narration_map={"solution 1":NarrationEvent(
                                        id = "solution 1",
                                        start_step="pythag solution DLL0",
                                        end_step="pythag solution DLL0",
                                        utterance="The solution to the problem is c = 5.",
                                        sync_map=None, # TODO
                                        duration=0.0
                                    )},
                                    next=None
                                )
                            )
                        )
                    )
                ),
                nodes = {},
                traversal_history = TraversalHistory(
                    history = []
                )
            )
            self.plan.nodes = {
                "pythag intro": self.plan.lesson_root,
                "pythag triangle": self.plan.lesson_root.next,
                "pythag problem": self.plan.lesson_root.next.next
            }
        else:
            raise Exception("Lesson not found") # TODO will fetch from db
        self.current_node_id = "pythag intro"
        return self.plan
    
    def get_current_node(self) -> LessonNode:
        return self.plan.nodes[self.current_node_id]
    
    def get_current_step(self) -> StepDLLNode:
        return self.get_current_node().get_current_step()
    
    def get_current_command_group(self) -> CommandGroup:
        return self.get_current_node().get_current_command_group()
    
    async def next_node(self):
        return await self.traversal_service.next_node(self.plan) # TODO
    
    async def execute_current_step(self):
        return await self.step_service.execute_step(
            self.get_current_step(),
            self.traversal_service.get_current_state()
        ) # TODO