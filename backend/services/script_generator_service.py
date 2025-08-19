from typing import Dict, Any
import requests
import json
from services.prompt_service import PromptService
# from services.rag_service import RAGService
from services.traversal_service import TraversalService
from services.context_service import ContextService
import os
# handles all things LLM related
## Includes RAG operations
## retrieving prompt
## outputting LLM response

class ScriptGeneratorService:
    def __init__(self, prompt_service: PromptService, traversal_service: TraversalService, context_service: ContextService):
        self.prompt_service = prompt_service
        self.api_key = os.getenv("OPENROUTER_API_KEY")  # TODO: Move to env
        self.model = "meta-llama/llama-4-scout:free"  # TODO: Make configurable
        # self.rag_service = rag_service
        self.traversal_service = traversal_service
        self.context_service = context_service

    async def retrieve_context(self, step_id: str) -> dict:
        """
        Retrieve all relevant context for a step using ContextService.
        """
        return await self.context_service.get_step_context(step_id)

    async def generate_script(self, type: str, step_id: str, **kwargs) -> str:
        """
        Generate a script using the LLM based on a prompt template and real context.
        """
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
                topic=context["topic"],
                step_description=context["step_description"],
                previous_context=context["previous_context"],
                board_state=context["board_state"]
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
        step_id: str
    ) -> str:
        """Generate a narration script using the narration prompt template and real context."""
        return await self.generate_script(
            "narration",
            step_id=step_id
        )

    async def handle_clarification(
        self,
        step_id: str
    ) -> str:
        """Handle clarification questions using the LLM and real context."""
        return await self.generate_script(
            "clarification",
            step_id=step_id
        ) 