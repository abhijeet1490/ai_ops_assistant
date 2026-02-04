from ..llm.llm_client import LLMClient
import json

class VerifierAgent:
    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client

    def verify_and_summarize(self, user_request: str, execution_results: dict):
        """
        Verifies the execution results against the user's initial request
        and generates a final natural language summary.
        """
        results_str = json.dumps(execution_results, indent=2)
        
        system_prompt = """
        You are a Verifier Agent.
        Your job is to review the results of tool executions performed to satisfy a user's request.
        
        1. Check if the tools executed successfully and returned relevant data.
        2. Synthesize the information into a clear, helpful, and polite response for the user.
        3. If any steps failed or if data is missing, explicitly mention what could not be completed.
        
        Do not output JSON. Output a natural language response.
        """
        
        user_prompt = f"""
        User Request: "{user_request}"
        
        Execution Results:
        {results_str}
        
        Please provide the final answer.
        """
        
        response = self.llm.generate_response(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            json_mode=False
        )
        
        return response
