from typing import Dict, Any
import requests
import json
from services.prompt_service import PromptService
from services.rag_service import RAGService
from services.traversal_service import TraversalService

# handles all things LLM related
## Includes RAG operations
## retrieving prompt
## outputting LLM response

class ScriptGeneratorService:
    def __init__(self, prompt_service: PromptService, rag_service: RAGService, traversal_service: TraversalService):
        self.prompt_service = prompt_service
        self.api_key = "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"  # TODO: Move to env
        self.model = "meta-llama/llama-4-scout:free"  # TODO: Make configurable
        self.rag_service = rag_service
        self.traversal_service = traversal_service

    async def retrieve_context(self, step_id: str) -> dict:
        # TODO
        return {
            "step_description": "Step description",
            "topic": "topic",
            "previous_context": "Previous context",
            "board_state": "Board state",
            "new_visual_elements": "New visual elements"
        }

    async def generate_script(self, type: str, step_id: str) -> str:
        """
        Generate a script using the LLM based on a prompt template
        
        Args:
            prompt_name: Name of the prompt template to use
            **kwargs: Variables to inject into the prompt template
        
        Returns:
            Generated script text
        """

        # TODO: add RAG operations

        # TODO: make a way to retrieve context based on step_id or other identifier
        context = await self.retrieve_context(step_id)

        if type == "narration":
            prompt = self.prompt_service.get_narration_prompt(
                topic=context["topic"],
                step_description=context["step_description"],
                previous_context=context["previous_context"],
                board_state=context["board_state"],
                new_visual_elements=context["new_visual_elements"]
            )
        elif type == "clarification":
            prompt = self.prompt_service.get_clarification_prompt(
                topic=topic,
                step_description=step_description,
                previous_context=previous_context,
                board_state=board_state
            )
        else:
            raise ValueError(f"Invalid script type: {type}")
        
        # Call the LLM API
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}"
            },
            data=json.dumps({
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            })
        )
        
        # Parse and return the response
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]

    async def generate_narration_script(
        self,
        topic: str,
        step_description: str,
        previous_context: str,
        board_state: str,
        new_visual_elements: str
    ) -> str:
        """Generate a narration script using the narration prompt template"""
        return await self.generate_script(
            "narration",
            topic=topic,
            step_description=step_description,
            previous_context=previous_context,
            board_state=board_state,
            new_visual_elements=new_visual_elements
        )

    async def handle_clarification(
        self,
        question: str,
        context: str,
        board_state: str,
    ) -> str:
        """Handle clarification questions using the LLM"""
        # TODO: Create a clarification prompt template
        return await self.generate_script(
            "clarification",  # You'll need to create this prompt template
            question=question,
            context=context,
            board_state=board_state,
        ) 