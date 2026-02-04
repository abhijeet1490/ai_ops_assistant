from openai import OpenAI
import os
import json

class LLMClient:
    def __init__(self):
        self.api_key = os.environ.get("OPEN_AI_KEY") or os.environ.get("OPENAI_API_KEY") 
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set.")
        self.client = OpenAI(api_key=self.api_key)

    def generate_response(self, system_prompt: str, user_prompt: str, json_mode: bool = False, model: str = "gpt-4o"):
        """
        Generates a response from the LLM.
        
        Args:
            system_prompt: The system instruction.
            user_prompt: The user's input/query.
            json_mode: If True, enforces valid JSON output.
            model: The model to use (default: gpt-4o).
            
        Returns:
            The content of the response message.
        """
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        kwargs = {
            "model": model,
            "messages": messages,
        }
        
        if json_mode:
            kwargs["response_format"] = {"type": "json_object"}

        try:
            response = self.client.chat.completions.create(**kwargs)
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"
