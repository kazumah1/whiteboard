import requests
import json
from typing import Dict, Any

class LLMConfig:
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

def generate_completion(prompt: str, config: LLMConfig) -> str:
    """
    Generate a completion using the LLM
    
    Args:
        prompt: The prompt to send to the LLM
        config: LLM configuration
        
    Returns:
        Generated text
    """
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {config.api_key}"
        },
        data=json.dumps({
            "model": config.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        })
    )
    
    response_data = response.json()
    return response_data["choices"][0]["message"]["content"] 