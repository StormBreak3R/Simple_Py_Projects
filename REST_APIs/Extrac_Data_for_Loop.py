"""
i got json data first then iterated over the
json data to gather the exact data we need
"""

import requests  # importing requests libraries
import json

response = requests.get("https://statsapi.web.nhl.com/api/v1/teams")  # sending request to the website
json_response = response.json()  # getting json data

for i in range(0, len(json_response["teams"])):  # using for loop to iterate over the json data
    team_name = json_response['teams'][i]["teamName"]
    time_zone_id = json_response['teams'][i]["venue"]["timeZone"]["id"]
    abbrev = json_response['teams'][i]["abbreviation"]

    team_data = {  # getting data in dictionary format
        "teamName": team_name,
        "timeZoneId": time_zone_id,
        "abbreviation": abbrev
     }
    print(team_data) # printing the data
