from pydantic import BaseModel
from typing import List
from models.whiteboard_command import WhiteboardCommand

class CommandGroup(BaseModel):
    id: str # unique id for the command group
    commands: List[WhiteboardCommand] # list of commands to be executed (e.g. strokes, shapes, etc.)
    current_command_index: int # index of the current command to be executed
    step_id: str # id of the DLL node that the command group belongs to

    def get_current_command(self) -> WhiteboardCommand:
        return self.commands[self.current_command_index]
    
    def next(self) -> WhiteboardCommand:
        self.current_command_index += 1
        return self.get_current_command()
    
    def undo(self) -> WhiteboardCommand:
        self.current_command_index -= 1
        return self.get_current_command()
    
    def reset(self) -> None:
        self.current_command_index = 0