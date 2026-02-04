# AI Operations Assistant

A multi-agent system designed to act as an intelligent operations assistant. It accepts natural language tasks, plans a sequence of actions, executes them using integrated tools (GitHub, OpenWeatherMap), and verifies the results to provide a comprehensive answer.

## Architecture

The system follows a three-stage multi-agent architecture:

1.  **Planner Agent**: Analyzes the user's request and breaks it down into a sequence of actionable steps (JSON plan). It selects the appropriate tools (`search_github`, `get_weather`) for each step.
2.  **Executor Agent**: Iterates through the plan, dynamically calling the selected tools from the registry and collecting their outputs.
3.  **Verifier Agent**: Reviews the original request and the execution results. It synthesizes the data into a final, natural language response and checks for any missing information.

## Integrated APIs

-   **GitHub API**: Allows searching for public repositories (name, stars, description).
-   **OpenWeatherMap API**: Provides current weather data for specified cities.

## Setup Instructions

1.  **Clone/Download the repository**.

2.  **Install Dependencies**:
    python 3.10+ is recommended.
    ```bash
    pip install -r ai_ops_assistant/requirements.txt
    ```

3.  **Configure Environment Variables**:
    Create a `.env` file in `ai_ops_assistant/` (or rename `.env.example` to `.env`) and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    GITHUB_TOKEN=your_github_token
    OPENWEATHER_API_KEY=your_openweather_api_key
    ```

## Running the Project

To start the web interface, run the following command from the root directory:

```bash
streamlit run ai_ops_assistant/app.py
```

## Example Prompts

Here are some example tasks you can try:

1.  *"Find the most popular Python weather library on GitHub and tell me the current weather in San Francisco."*
2.  *"Search for a machine learning repository related to 'transformers' and check the weather in London."*
3.  *"Find a React UI library and get the weather details for Tokyo."*

## Project Structure

```text
ai_ops_assistant/
├── agents/             # Agent implementations
│   ├── planner.py
│   ├── executor.py
│   └── verifier.py
├── tools/              # Tool integrations
│   ├── github_tool.py
│   ├── weather_tool.py
│   └── registry.py
├── llm/                # LLM client wrapper
│   └── llm_client.py
├── app.py              # Streamlit frontend
├── main.py             # Main orchestration logic
├── requirements.txt
├── .env.example
└── README.md
```
