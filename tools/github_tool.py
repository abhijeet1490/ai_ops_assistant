import requests
import os

class GitHubTool:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.token = os.environ.get("GITHUB_TOKEN")
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if self.token:
            self.headers["Authorization"] = f"token {self.token}"

    def search_repositories(self, query: str):
        """
        Searches for GitHub repositories matching the query.
        Returns a list of dictionaries with name, stars, and description.
        """
        try:
            url = f"{self.base_url}/search/repositories"
            params = {"q": query, "sort": "stars", "order": "desc", "per_page": 5}
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            results = []
            for item in data.get("items", []):
                results.append({
                    "name": item.get("full_name"),
                    "stars": item.get("stargazers_count"),
                    "description": item.get("description"),
                    "url": item.get("html_url")
                })
            return results
        except requests.exceptions.RequestException as e:
            return {"error": f"GitHub API request failed: {str(e)}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}
