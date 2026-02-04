import requests
import os

class WeatherTool:
    def __init__(self):
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = os.environ.get("OPENWEATHER_API_KEY")

    def get_weather(self, city: str):
        """
        Fetches current weather for a given city using OpenWeatherMap.
        Returns a dictionary with temperature (Celsius) and description.
        """
        if not self.api_key:
            return {"error": "OPENWEATHER_API_KEY not found in environment variables."}

        try:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            weather_desc = data["weather"][0]["description"] if data.get("weather") else "No description"
            temp = data["main"]["temp"] if data.get("main") else "N/A"
            
            return {
                "city": city,
                "temperature_celsius": temp,
                "description": weather_desc
            }
        except requests.exceptions.RequestException as e:
             return {"error": f"Weather API request failed: {str(e)}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}
