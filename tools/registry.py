from .github_tool import GitHubTool
from .weather_tool import WeatherTool

def get_tool_registry():
    """
    Returns a dictionary mapping tool names to their callable functions.
    This allows agents to dynamically select and execute tools.
    """
    github_tool = GitHubTool()
    weather_tool = WeatherTool()

    return {
        "search_github": github_tool.search_repositories,
        "get_weather": weather_tool.get_weather
    }
