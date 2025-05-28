from pathlib import Path
from typing import Dict, Any

class PromptService:
    def __init__(self):
        self.prompts_dir = Path(__file__).parent.parent / "prompts"
        self._load_prompts()

    def _load_prompts(self):
        """Load all prompt templates from the prompts directory"""
        self.prompts = {}
        for prompt_file in self.prompts_dir.glob("*.txt"):
            with open(prompt_file, "r") as f:
                self.prompts[prompt_file.stem] = f.read()

    def get_prompt(self, prompt_name: str, **kwargs: Any) -> str:
        """
        Get a formatted prompt with variables replaced
        
        Args:
            prompt_name: Name of the prompt file (without .txt extension)
            **kwargs: Variables to inject into the prompt template
        
        Returns:
            Formatted prompt string
        """
        if prompt_name not in self.prompts:
            raise ValueError(f"Prompt '{prompt_name}' not found")
        
        template = self.prompts[prompt_name]
        return template.format(**kwargs)

    def get_narration_prompt(
        self,
        topic: str,
        step_description: str,
        previous_context: str,
        board_state: str,
        new_visual_elements: str
    ) -> str:
        """Get a formatted narration prompt"""
        return self.get_prompt(
            "narration",
            topic=topic,
            step_description=step_description,
            previous_context=previous_context,
            board_state=board_state,
            new_visual_elements=new_visual_elements
        )
    
    def get_clarification_prompt(
        self,
        topic: str,
        step_description: str,
        previous_context: str,
        board_state: str,
    ) -> str:
        """Get a formatted clarification prompt"""
        return self.get_prompt(
            "clarification",
            topic=topic,
            step_description=step_description,
            previous_context=previous_context,
            board_state=board_state
        )