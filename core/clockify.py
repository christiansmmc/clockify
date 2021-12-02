from config import API_KEY, WORKSPACE_ID
import requests
import calendar
from datetime import datetime
import json


class Clockify:
    def __init__(self):
        self.url = f'https://reports.api.clockify.me/v1/workspaces/{WORKSPACE_ID}/reports/summary'
        self.headers = {'X-Api-Key': API_KEY, 'Content-type': 'application/json'}

        last_month = datetime.now().month - 1
        year = datetime.now().year
        last_day_of_month = calendar.monthrange(year, last_month)

        initial_date = str(datetime(int(year), int(last_month), 1)).replace(" ", "T")
        final_date = str(datetime(int(year), int(last_month), int(last_day_of_month[1]))).replace(" ", "T").replace(
            "00:00:00", "23:59:59")

        self.data = {
            "exportType": "JSON",
            "dateRangeStart": initial_date,
            "dateRangeEnd": final_date,
            "amountShown": "HIDE_AMOUNT",
            "summaryFilter": {
                "groups": [
                    "USER"
                ]
            }
        }

    def get_time_entry(self):
        response = requests.post(self.url, headers=self.headers, data=json.dumps(self.data))
        return json.loads(response.content)['groupOne']
