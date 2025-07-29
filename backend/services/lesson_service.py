from models.lesson_plan import LessonPlan
from models.lesson_node import LessonNode
from models.step_node import StepDLLNode
from models.command_group import CommandGroup
from models.whiteboard_command import WhiteboardCommand
from models.whiteboard_object import ExcalidrawElement
from typing import Dict

class LessonService:
    def __init__(self):
        self.plan: LessonPlan | None = None
        self.current_node_id: str | None = None
        self.current_step_id: str | None = None

    def build_hardcoded_lesson(self):
        # 1. Elements
        el1 = ExcalidrawElement(
            id="el1",
            type="text",
            x=100,
            y=100,
            width=250,
            height=30,
            angle=0,
            strokeColor="#f8f9fa",
            backgroundColor="transparent",
            fillStyle="solid",
            strokeWidth=1,
            strokeStyle="solid",
            roughness=1,
            opacity=100,
            seed=1,
            version=1,
            versionNonce=1,
            isDeleted=False,
            groupIds=[],
            updated=1234567890,
            locked=False,
            text="Pythagorean Theorem",
            fontSize=24,
            textAlign="left",
            verticalAlign="top",
        )
        el2 = ExcalidrawElement(
            id="el2",
            type="line",
            x=100,
            y=50,
            width=100,
            height=100,
            angle=0,
            strokeColor="#f8f9fa",
            backgroundColor="transparent",
            fillStyle="solid",
            strokeWidth=2,
            strokeStyle="solid",
            roughness=1,
            opacity=100,
            seed=2,
            version=1,
            versionNonce=2,
            isDeleted=False,
            groupIds=[],
            updated=1234567891,
            locked=False,
            points=[[0,0],[100,0],[100,100],[0,100]],
        )
        el3 = ExcalidrawElement(
            id="el3",
            type="text",
            x=100,
            y=100,
            width=200,
            height=30,
            angle=0,
            strokeColor="#f8f9fa",
            backgroundColor="transparent",
            fillStyle="solid",
            strokeWidth=1,
            strokeStyle="solid",
            roughness=1,
            opacity=100,
            seed=1,
            version=1,
            versionNonce=1,
            isDeleted=False,
            groupIds=[],
            updated=1234567890,
            locked=False,
            text="Pythagorean Theorem Step 2",
            fontSize=24,
            textAlign="left",
            verticalAlign="top",
        )
        # 2. Commands
        cmd1 = WhiteboardCommand(id="cmd1", element_id="el1")
        cmd2 = WhiteboardCommand(id="cmd2", element_id="el2")
        cmd3 = WhiteboardCommand(id="cmd3", element_id="el3")
        # 3. Command Groups
        cg1 = CommandGroup(id="cg1", command_ids=["cmd1"], current_command_index=0, step_id="step1")
        cg2 = CommandGroup(id="cg2", command_ids=["cmd2"], current_command_index=0, step_id="step2")
        cg3 = CommandGroup(id="cg3", command_ids=["cmd3"], current_command_index=0, step_id="step3")
        # 4. Steps
        # TODO: right now, next_id parameter causes multiple elements to be rendered in - might have to be changed
        step1 = StepDLLNode(id="step1", command_group_ids=["cg1"])
        step2 = StepDLLNode(id="step2", prev_id="step1", command_group_ids=["cg2"])
        step3 = StepDLLNode(id="step3", prev_id="step2", command_group_ids=["cg3"])
        # 5. Nodes
        node1 = LessonNode(id="node1", steps_DLL_root_id="step1", next_id="node2")
        node2 = LessonNode(id="node2", steps_DLL_root_id="step2", next_id="node3")
        node3 = LessonNode(id="node3", steps_DLL_root_id="step3")
        # 6. Build dicts
        elements = {e.id: e for e in [el1, el2, el3]}
        commands = {c.id: c for c in [cmd1, cmd2, cmd3]}
        command_groups = {cg.id: cg for cg in [cg1, cg2, cg3]}
        steps = {s.id: s for s in [step1, step2, step3]}
        nodes = {n.id: n for n in [node1, node2, node3]}
        # 7. Create lesson plan
        self.plan = LessonPlan(
            id="pythagorean-theorem",
            title="Pythagorean Theorem",
            nodes=nodes,
            steps=steps,
            command_groups=command_groups,
            commands=commands,
            elements=elements,
        )
        self.current_node_id = "node1"
        self.current_step_id = "step1"

    def get_lesson_from_db(self, lesson_id: str) -> LessonPlan:
        pass

    def generate_lesson(self, lesson_id: str):
        pass

    def load_lesson(self, lesson_id: str) -> LessonPlan:
        if self.plan is None or self.plan.id != lesson_id:
            self.build_hardcoded_lesson()
        # else:
        #     self.plan = self.get_lesson_from_db(lesson_id)
        # if self.plan is None:
        #     self.generate_lesson(lesson_id)
        # make sure to set self.current_node_id and self.current_step_id
        return self.plan

    def get_current_node(self) -> LessonNode:
        return self.plan.nodes[self.current_node_id]

    # moves to next node and returns
    def get_next_node(self) -> LessonNode | None:
        node = self.get_current_node()
        if node.next_id:
            self.current_node_id = node.next_id
            return self.plan.nodes[self.current_node_id]
        return None
    

    def get_steps_for_node(self, node_id: str) -> list[StepDLLNode]:
        node = self.plan.nodes[node_id]
        steps = []
        step_id = node.steps_DLL_root_id
        while step_id:
            step = self.plan.steps[step_id]
            steps.append(step)
            step_id = step.next_id
        return steps
    
    def get_current_step(self):
        return self.plan.steps[self.current_step_id]

    def get_command_groups_for_step(self, step_id: str) -> list[CommandGroup]:
        step = self.plan.steps[step_id]
        return [self.plan.command_groups[cg_id] for cg_id in step.command_group_ids]

    def get_commands_for_group(self, group_id: str) -> list[WhiteboardCommand]:
        group = self.plan.command_groups[group_id]
        return [self.plan.commands[cid] for cid in group.command_ids]

    def get_elements_for_node(self, node_id: str) -> list[ExcalidrawElement]:
        elements = []
        for step in self.get_steps_for_node(node_id):
            for group in self.get_command_groups_for_step(step.id):
                for cmd in self.get_commands_for_group(group.id):
                    elements.append(self.plan.elements[cmd.element_id])
        return elements