from .llm.llm_client import LLMClient
from .agents.planner import PlannerAgent
from .agents.executor import ExecutorAgent
from .agents.verifier import VerifierAgent
import os

class AIOpsAssistant:
    def __init__(self):
        # Ensure API keys are present (usually loaded by app.py via dotenv, 
        # but good to check or let LLMClient handle it)
        try:
            self.llm_client = LLMClient()
        except ValueError as e:
            raise ValueError(f"Initialization Error: {e}")

        self.planner = PlannerAgent(self.llm_client)
        self.executor = ExecutorAgent()
        self.verifier = VerifierAgent(self.llm_client)

    def run(self, user_query: str):
        """
        Orchestrates the agentic workflow: Plan -> Execute -> Verify.
        """
        print(f"--- Starting Task: {user_query} ---")

        # 1. Planner
        print("1. Planning...")
        plan = self.planner.plan_task(user_query)
        
        # 2. Executor
        print("2. Executing...")
        execution_results = self.executor.execute_plan(plan)
        
        # 3. Verifier
        print("3. Verifying...")
        final_response = self.verifier.verify_and_summarize(user_query, execution_results)
        
        print("--- Task Complete ---")
        
        return {
            "plan": plan,
            "execution_results": execution_results,
            "final_response": final_response
        }
