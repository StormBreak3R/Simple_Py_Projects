"""
i have used nested for loop for extracting data
"""
import requests
result = requests.get("https://statsapi.web.nhl.com/api/v1/teams.json")
data = result.json()

team_count = 1

for item in data["teams"]:
    print(f"Team: {team_count}")
    print("Team Name: " + item["teamName"])
    print("Abbreviation: " + item["abbreviation"])
    venue = item["venue"]
    timeZone = venue["timeZone"]
    for tz in timeZone:
        print("TimeZone ID: " + timeZone["id"])
        team_count += 1
        print()
        break
