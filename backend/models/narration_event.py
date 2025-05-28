from pydantic import BaseModel
from typing import List, Tuple

class NarrationEvent(BaseModel):
    id: str # unique id for the narration event
    start_step: str # start DLL step id
    end_step: str # end DLL step id
    utterance: str # words to be narrated
    sync_map: List[Tuple[str, float]] | None = None # DLL step id : time offset in seconds
    duration: float # duration of the narration event in seconds