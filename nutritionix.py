import requests
import os


class Nutritionix:
    def __init__(self, user_input):
        self.APP_ID = os.environ.get("APP_ID")
        self.API_KEY = os.environ.get("API_KEY")
        self.nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.user_input = user_input

        self.headers = {
            "x-app-id": self.APP_ID,
            "x-app-key": self.API_KEY
        }

    def exercises(self):
        nutritionix_info = {
            "query": self.user_input
        }
        response = requests.post(url=self.nutritionix_endpoint, json=nutritionix_info, headers=self.headers)
        response.raise_for_status()
        return response.json()['exercises']
