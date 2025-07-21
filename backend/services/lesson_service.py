from models.lesson_plan import LessonPlan
from models.traversal_history import TraversalHistory
from models.traversal_state import TraversalState
from models.lesson_node import LessonNode
from models.step_node import StepDLLNode
from models.command_group import CommandGroup
from models.whiteboard_command import WhiteboardCommand
from models.whiteboard_object import ExcalidrawElement
from models.narration_event import NarrationEvent
from services.traversal_service import TraversalService
from services.step_service import StepService
import time

# handles creating a lesson and getting positional information (for traversal and frontend)

class LessonService:
    def __init__(self, traversal_service: TraversalService, step_service: StepService):
        self.plan: LessonPlan | None = None
        self.current_node_id: str | None = None
        self.traversal_history: TraversalHistory | None = None
        self.traversal_service = traversal_service
        self.step_service = step_service

    def load_lesson(self, lesson_id: str, debug: bool = False) -> LessonPlan:
        if debug: # eventually check if lesson doesn't exists in db
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
                                element=ExcalidrawElement(
                                    id="intro-command-1",
                                    type="text",
                                    x=100,
                                    y=100,
                                    width=200,
                                    height=30,
                                    text="Pythagorean Theorem",
                                    fontSize=24,
                                    fontFamily=1,
                                    textAlign="left",
                                    verticalAlign="top",
                                    strokeColor="#000000",
                                    backgroundColor="transparent",
                                    strokeWidth=1,
                                    strokeStyle="solid",
                                    fillStyle="hachure",
                                    roughness=1,
                                    opacity=100,
                                    angle=0,
                                    groupIds=[],
                                    strokeSharpness="sharp",
                                    seed=1,
                                    version=1,
                                    versionNonce=1,
                                    isDeleted=False,
                                    locked=False,
                                    updated=int(time.time() * 1000),
                                    commentCount=0,
                                    baseline=20,
                                    lineHeight=1.25,
                                    containerId=None,
                                    originalText="Pythagorean Theorem",
                                ),
                                delay=0.0,
                                duration=None,
                                step_id="intro DLL0",
                                narration_tag=None,
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
                                    element=ExcalidrawElement(
                                        id="triangle-command-1",
                                        type="line",
                                        x=100,
                                        y=50,
                                        width=100,
                                        height=100,
                                        points=[[0,0],[100,0],[100,100],[0,100]],
                                        strokeColor="#000000",
                                        backgroundColor="transparent",
                                        strokeWidth=2,
                                        strokeStyle="solid",
                                        fillStyle="hachure",
                                        roughness=1,
                                        opacity=100,
                                        angle=0,
                                        groupIds=[],
                                        strokeSharpness="sharp",
                                        seed=1,
                                        version=1,
                                        versionNonce=1,
                                        isDeleted=False,
                                        locked=False,
                                        updated=int(time.time() * 1000),
                                        commentCount=0,
                                        startArrowhead=None,
                                        endArrowhead=None,
                                        startBinding=None,
                                        endBinding=None,
                                    ),
                                    delay=1.0,
                                    duration=None,
                                    step_id="pythag triangle DLL0",
                                    narration_tag=None,
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
                                    commands=[
                                        WhiteboardCommand(
                                            element=ExcalidrawElement(
                                                id="problem-command-1",
                                                type="text",
                                                x=100,
                                                y=50,
                                                text="3",
                                                fontSize=24,
                                                strokeColor="#000000",
                                                isDeleted=False,
                                            ),
                                            step_id="pythag problem DLL0"
                                        ),
                                        WhiteboardCommand(
                                            element=ExcalidrawElement(
                                                id="problem-command-2",
                                                type="text",
                                                x=110,
                                                y=50,
                                                text="4",
                                                fontSize=24,
                                                strokeColor="#000000",
                                                isDeleted=False,
                                            ),
                                            step_id="pythag problem DLL0"
                                        ),
                                        WhiteboardCommand(
                                            element=ExcalidrawElement(
                                                id="problem-command-3",
                                                type="text",
                                                x=120,
                                                y=50,
                                                text="c",
                                                fontSize=24,
                                                strokeColor="#000000",
                                                isDeleted=False,
                                            ),
                                            step_id="pythag problem DLL0"
                                        )
                                    ],
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
                                            element=ExcalidrawElement(
                                                id="formula-command-1",
                                                type="text",
                                                x=100,
                                                y=50,
                                                text="a^2 + b^2 = c^2",
                                                fontSize=24,
                                                strokeColor="#000000",
                                                isDeleted=False,
                                            ),
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
                                            commands=[
                                                WhiteboardCommand(
                                                    element=ExcalidrawElement(
                                                        id="solution-command-1",
                                                        type="text",
                                                        x=100,
                                                        y=50,
                                                        text="3^2 + 4^2 = c^2",
                                                        fontSize=24,
                                                        strokeColor="#000000",
                                                        isDeleted=False,
                                                    ),
                                                    step_id="pythag solution DLL0"
                                                ),
                                                WhiteboardCommand(
                                                    element=ExcalidrawElement(
                                                        id="solution-command-2",
                                                        type="text",
                                                        x=100,
                                                        y=50,
                                                        text="9 + 16 = c^2",
                                                        fontSize=24,
                                                        strokeColor="#000000",
                                                        isDeleted=False,
                                                    ),
                                                    step_id="pythag solution DLL0"
                                                ),
                                                WhiteboardCommand(
                                                    element=ExcalidrawElement(
                                                        id="solution-command-3",
                                                        type="text",
                                                        x=100,
                                                        y=50,
                                                        text="25 = c^2",
                                                        fontSize=24,
                                                        strokeColor="#000000",
                                                        isDeleted=False,
                                                    ),
                                                    step_id="pythag solution DLL0"
                                                ),
                                                WhiteboardCommand(
                                                    element=ExcalidrawElement(
                                                        id="solution-command-4",
                                                        type="text",
                                                        x=100,
                                                        y=50,
                                                        text="c = 5",
                                                        fontSize=24,
                                                        strokeColor="#1971c2",
                                                        isDeleted=False,
                                                    ),
                                                    step_id="pythag solution DLL0"
                                                )
                                            ],
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
            
            # Initialize current_step for each lesson node
            self.plan.lesson_root.current_step = self.plan.lesson_root.steps_DLL_root
            if self.plan.lesson_root.next:
                self.plan.lesson_root.next.current_step = self.plan.lesson_root.next.steps_DLL_root
                if self.plan.lesson_root.next.next:
                    self.plan.lesson_root.next.next.current_step = self.plan.lesson_root.next.next.steps_DLL_root
                    if self.plan.lesson_root.next.next.next:
                        self.plan.lesson_root.next.next.next.current_step = self.plan.lesson_root.next.next.next.steps_DLL_root
                        if self.plan.lesson_root.next.next.next.next:
                            self.plan.lesson_root.next.next.next.next.current_step = self.plan.lesson_root.next.next.next.next.steps_DLL_root
            
            self.plan.nodes = {
                "pythag intro": self.plan.lesson_root,
                "pythag triangle": self.plan.lesson_root.next,
                "pythag problem": self.plan.lesson_root.next.next,
                "pythag formula": self.plan.lesson_root.next.next.next,
                "pythag solution": self.plan.lesson_root.next.next.next.next
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
    
    def next_node(self) -> LessonNode | None:
        """
        Move to the next LessonNode (concept) in the DAG.
        Resets to the first step of the new node and updates traversal state/history.
        Returns the new LessonNode, or None if at the end.
        """
        next_node = self.get_current_node().next
        if next_node is not None:
            self.current_node_id = next_node.id
            # Reset to the first step of the new node
            next_node.current_step = next_node.steps_DLL_root
            self.traversal_service.set_current_state(TraversalState(
                current_node_id=self.current_node_id,
                current_step_id=next_node.get_current_step().id,
                narration_event_id=None, # TODO: set if needed
            ))
            return next_node
        return None

    def prev_node(self) -> LessonNode | None:
        """
        Move to the previous LessonNode (concept) in the DAG.
        Resets to the first step of the new node and updates traversal state/history.
        Returns the new LessonNode, or None if at the beginning.
        """
        prev_node = getattr(self.get_current_node(), 'prev', None)
        if prev_node is not None:
            self.current_node_id = prev_node.id
            prev_node.current_step = prev_node.steps_DLL_root
            self.traversal_service.set_current_state(TraversalState(
                current_node_id=self.current_node_id,
                current_step_id=prev_node.get_current_step().id,
                narration_event_id=None,
            ))
            return prev_node
        return None
    
    def get_current_node_id(self) -> str:
        return self.current_node_id
    
    def get_current_step_id(self) -> str:
        return self.get_current_step().id
    
    def next_step(self) -> StepDLLNode | None:
        """
        Move to the next step in the current LessonNode's DLL.
        Updates the current step pointer and traversal state/history.
        Returns the new StepDLLNode, or None if at the end.
        """
        current_node = self.get_current_node()
        current_step = current_node.get_current_step()
        next_step = self.step_service.next_step(current_step)
        if next_step is not None:
            current_node.current_step = next_step
            self.traversal_service.set_current_state(TraversalState(
                current_node_id=self.current_node_id,
                current_step_id=next_step.id,
                narration_event_id=None,
            ))
            return next_step
        return None

    def prev_step(self) -> StepDLLNode | None:
        """
        Move to the previous step in the current LessonNode's DLL.
        Updates the current step pointer and traversal state/history.
        Returns the new StepDLLNode, or None if at the beginning.
        """
        current_node = self.get_current_node()
        current_step = current_node.get_current_step()
        prev_step = self.step_service.prev_step(current_step)
        if prev_step is not None:
            current_node.current_step = prev_step
            self.traversal_service.set_current_state(TraversalState(
                current_node_id=self.current_node_id,
                current_step_id=prev_step.id,
                narration_event_id=None,
            ))
            return prev_step
        return None
    
    
    async def execute_current_step(self):
        return self.step_service.execute_step(
            self.get_current_step(),
            self.traversal_service.get_current_state()
        ) # TODO

    async def execute_step(self, lesson_id: str, step_index: int):
        """Execute a specific step by index and return the whiteboard elements."""
        try:
            print(f"Executing step {step_index} for lesson {lesson_id}")
            
            # Load the lesson if not already loaded
            if not self.plan or self.plan.id != lesson_id:
                print("Loading lesson...")
                self.load_lesson(lesson_id, debug=True)
            
            # Navigate to the specified step
            current_node = self.get_current_node()
            print(f"Current node: {current_node.id}")
            
            current_step = current_node.steps_DLL_root
            print(f"Starting with root step: {current_step.id}")
            
            # Navigate to the specified step index
            for i in range(step_index):
                print(f"Navigating to step {i}...")
                if current_step.next:
                    current_step = current_step.next
                    print(f"Moved to step: {current_step.id}")
                else:
                    print("No next step available")
                    break
            
            # Set the current step
            current_node.current_step = current_step
            print(f"Set current step to: {current_step.id}")
            
            # Initialize traversal state if it doesn't exist
            if not self.traversal_service.get_current_state():
                print("Initializing traversal state...")
                self.traversal_service.set_current_state(TraversalState(
                    current_node_id=self.current_node_id,
                    current_step_id=current_step.id,
                    narration_event_id=None,
                ))
            
            # Execute the step
            print("Calling step service...")
            elements = self.step_service.execute_step(
                current_step,
                self.traversal_service.get_current_state()
            )
            
            print(f"Returning {len(elements)} elements")
            return elements
            
        except Exception as e:
            print(f"Error in execute_step: {e}")
            import traceback
            traceback.print_exc()
            raise