import os
import requests
from datetime import datetime


class Sheet:
    def __init__(self):
        self.header = {
            "Authorization": os.environ.get("SHEET_AUTHORIZATION")
        }

    def post(self, exercises):
        sheet_endpoint = os.environ.get("SHEET_ENDPOINT")
        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")
        for exercise in exercises:
            post_info = {
                "workout":
                    {
                        "date": date,
                        "time": time,
                        "exercise": exercise['name'],
                        "duration": exercise['duration_min'],
                        "calories": exercise['nf_calories'],
                        "id": exercise['tag_id']
                    }
            }

            response = requests.post(url=sheet_endpoint, json=post_info, headers=self.header)
            response.raise_for_status()
            print(response.text)
