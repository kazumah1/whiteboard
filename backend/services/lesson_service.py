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
        el4 = ExcalidrawElement(
            id= "el4",
            type= "rectangle",
            x= 0,
            y= 0,
            width= 100,
            height= 60,
            angle= 0,
            strokeColor= "#fffffff",
            backgroundColor= "#e0e0e0",
            fillStyle= "solid",
            strokeWidth= 1,
            strokeStyle= "solid",
            roughness= 1,
            opacity= 100,
            seed= 123,
            version= 1,
            versionNonce= 1,
            isDeleted= False,
            groupIds= [],
            updated= 1234567890,
            locked= False,
        )
        el5 = ExcalidrawElement(
            id= "el5",
            type= "rectangle",
            x= 100,
            y= 50,
            width= 60,
            height= 100,
            angle= 0,
            strokeColor= "#2f9e44",
            backgroundColor= "#e0e0e0",
            fillStyle= "solid",
            strokeWidth= 1,
            strokeStyle= "solid",
            roughness= 1,
            opacity= 100,
            seed= 123,
            version= 1,
            versionNonce= 1,
            isDeleted= False,
            groupIds= [],
            updated= 1234567890,
            locked= False,
        )
        el6 = ExcalidrawElement(
            id= "el6",
            type= "rectangle",
            x= 100,
            y= 100,
            width= 60,
            height= 60,
            angle= 0,
            strokeColor= "#ffa94d",
            backgroundColor= "#e0e0e0",
            fillStyle= "solid",
            strokeWidth= 1,
            strokeStyle= "solid",
            roughness= 1,
            opacity= 100,
            seed= 123,
            version= 1,
            versionNonce= 1,
            isDeleted= False,
            groupIds= [],
            updated= 1234567890,
            locked= False,
        )
        el7 = ExcalidrawElement(
            id= "el7",
            type= "rectangle",
            x= 40,
            y= 40,
            width= 80,
            height= 80,
            angle= 0,
            strokeColor= "#be4bdb",
            backgroundColor= "#e0e0e0",
            fillStyle= "solid",
            strokeWidth= 1,
            strokeStyle= "solid",
            roughness= 1,
            opacity= 100,
            seed= 123,
            version= 1,
            versionNonce= 1,
            isDeleted= False,
            groupIds= [],
            updated= 1234567890,
            locked= False,
        )
        el8 = ExcalidrawElement(
            id= "el8",
            type= "rectangle",
            x= 50,
            y= 50,
            width= 10,
            height= 10,
            angle= 0,
            strokeColor= "#12b886",
            backgroundColor= "#e0e0e0",
            fillStyle= "solid",
            strokeWidth= 1,
            strokeStyle= "solid",
            roughness= 1,
            opacity= 100,
            seed= 123,
            version= 1,
            versionNonce= 1,
            isDeleted= False,
            groupIds= [],
            updated= 1234567890,
            locked= False,
        )
        # 2. Commands
        cmd1 = WhiteboardCommand(id="cmd1", element_id="el1")
        cmd2 = WhiteboardCommand(id="cmd2", element_id="el2")
        cmd3 = WhiteboardCommand(id="cmd3", element_id="el3")
        cmd4 = WhiteboardCommand(id="cmd4", element_id="el4")
        cmd5 = WhiteboardCommand(id="cmd5", element_id="el5")
        cmd6 = WhiteboardCommand(id="cmd6", element_id="el6")
        cmd7 = WhiteboardCommand(id="cmd7", element_id="el7")
        cmd8 = WhiteboardCommand(id="cmd8", element_id="el8")
        # 3. Command Groups
        cg1 = CommandGroup(id="cg1", command_ids=["cmd1"], current_command_index=0, step_id="step1")
        cg2 = CommandGroup(id="cg2", command_ids=["cmd2"], current_command_index=0, step_id="step2")
        cg3 = CommandGroup(id="cg3", command_ids=["cmd3"], current_command_index=0, step_id="step3")
        cg4 = CommandGroup(id="cg4", command_ids=["cmd4", "cmd8"], current_command_index=0, step_id="step4")
        cg5 = CommandGroup(id="cg5", command_ids=["cmd5"], current_command_index=0, step_id="step5")
        cg6 = CommandGroup(id="cg6", command_ids=["cmd6"], current_command_index=0, step_id="step6")
        cg7 = CommandGroup(id="cg7", command_ids=["cmd7"], current_command_index=0, step_id="step6")
        # 4. Steps
        # TODO: right now, next_id parameter causes multiple elements to be rendered in - might have to be changed
        step1 = StepDLLNode(id="step1", next_id="step2", command_group_ids=["cg1"])
        step2 = StepDLLNode(id="step2", prev_id="step1", next_id="step3", command_group_ids=["cg2"])
        step3 = StepDLLNode(id="step3", prev_id="step2", next_id="step4", command_group_ids=["cg3"])
        step4 = StepDLLNode(id="step4", prev_id="step3", next_id="step5", command_group_ids=["cg4"])
        step5 = StepDLLNode(id="step5", prev_id="step4", next_id="step6", command_group_ids=["cg5"])
        step6 = StepDLLNode(id="step6", prev_id="step5", command_group_ids=["cg6", "cg7"])
        # 5. Nodes
        node1 = LessonNode(id="node1", steps_DLL_root_id="step1", next_id="node2")
        node2 = LessonNode(id="node2", steps_DLL_root_id="step3", next_id="node3")
        node3 = LessonNode(id="node3", steps_DLL_root_id="step6")
        # 6. Build dicts
        elements = {e.id: e for e in [el1, el2, el3, el4, el5, el6, el7, el8]}
        commands = {c.id: c for c in [cmd1, cmd2, cmd3, cmd4, cmd5, cmd6, cmd7, cmd8]}
        command_groups = {cg.id: cg for cg in [cg1, cg2, cg3, cg4, cg5, cg6, cg7]}
        steps = {s.id: s for s in [step1, step2, step3, step4, step5, step6]}
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

    # traverses to and returns the next lesson node
    def next_node(self) -> LessonNode | None:
        node = self.get_current_node()
        if node.next_id:
            self.current_node_id = node.next_id
            return self.get_current_node()
        return None
    
    # returns all step nodes for current lesson node (TODO: used for when going back to prev nodes in history)
    def get_steps_for_node(self, node_id: str) -> list[StepDLLNode]:
        node = self.plan.nodes[node_id]
        steps = []
        step_id = node.steps_DLL_root_id
        while step_id:
            step = self.plan.steps[step_id]
            steps.append(step)
            step_id = step.next_id
        return steps
    
    # returns the current step node
    def get_current_step(self):
        return self.plan.steps[self.current_step_id]
    
    # traverse to and returns the next step node
    def next_step(self):
        step = self.get_current_step()
        if step.next_id:
            print('next step exists')
            self.current_step_id = step.next_id
            return self.get_current_step()
        print('no next step')
        return None
    
    # traverse to and returns the previous step node
    def prev_step(self):
        step = self.get_current_step()
        if step.prev_id:
            self.current_step_id = step.prev_id
            return self.get_current_step()
        return None

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
    
    def get_elements_for_step(self, step_id: str) -> list[ExcalidrawElement]:
        elements = []
        for group in self.get_command_groups_for_step(step_id):
            for cmd in self.get_commands_for_group(group.id):
                elements.append(self.plan.elements[cmd.element_id])
        return elements