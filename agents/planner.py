import json
from ..llm.llm_client import LLMClient

class PlannerAgent:
    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client

    def plan_task(self, user_request: str):
        """
        Generates a verified execution plan for the given user request.
        Returns a list of steps, where each step obeys the tool execution schema.
        """
        system_prompt = """
        You are a Planner Agent for an AI Operations Assistant.
        Your goal is to break down a user's natural language request into a sequence of actionable steps.

        Available Tools:
        1. "search_github":
           - Description: Search for GitHub repositories.
           - Arguments: {"query": "string"}
        2. "get_weather":
           - Description: Get the current weather for a specific city.
           - Arguments: {"city": "string"}

        Output Schema:
        You MUST return a JSON object with a key "steps" which is a list.
        Each item in the list must be an object with:
        - "tool_name": The exact name of the tool to use (e.g., "search_github").
        - "arguments": A dictionary of arguments for that tool.

        Example Output:
        {
            "steps": [
                {
                    "tool_name": "search_github",
                    "arguments": {"query": "python weather api"}
                },
                {
                    "tool_name": "get_weather",
                    "arguments": {"city": "London"}
                }
            ]
        }
        """
        
        response = self.llm.generate_response(
            system_prompt=system_prompt,
            user_prompt=user_request,
            json_mode=True
        )

        try:
            plan = json.loads(response)
            return plan.get("steps", [])
        except json.JSONDecodeError:
            return [{"error": "Failed to parse Planner output as JSON", "raw_output": response}]
