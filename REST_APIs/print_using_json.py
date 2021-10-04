import requests
import json

response = requests.get("https://statsapi.web.nhl.com/api/v1/teams")
json_response = response.json()

for i in range(0, len(json_response["teams"])):
    team_name = json_response['teams'][i]["teamName"]
    time_zone_id = json_response['teams'][i]["venue"]["timeZone"]["id"]
    abbrev = json_response['teams'][i]["abbreviation"]

    team_data = {
        "teamName": team_name,
        "timeZoneId": time_zone_id,
        "abbreviation": abbrev
     }

    print(json.dumps(team_data, indent=2))