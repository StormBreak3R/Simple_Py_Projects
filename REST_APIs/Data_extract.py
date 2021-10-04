"""
i have done this data extraction without using loop
its a basic one, hopefully everyone will understand this easily.
"""

import requests
result = requests.get("https://statsapi.web.nhl.com/api/v1/teams.json")

data = result.json()


def team1():
    team_name = data["teams"][0]["teamName"]
    t_z_id = data["teams"][0]["venue"]["timeZone"]["id"]
    abbreviation = data["teams"][0]["abbreviation"]

    data_1 = {
        "Team Name": team_name,
        "TimeZoneID": t_z_id,
        "Abbreviation": abbreviation
    }

    print(data_1)


def team2():
    team_name = data["teams"][1]["teamName"]
    t_z_id = data["teams"][1]["venue"]["timeZone"]["id"]
    abbreviation = data["teams"][1]["abbreviation"]

    data_2 = {
        "Team Name": team_name,
        "TimeZoneID": t_z_id,
        "Abbreviation": abbreviation
    }

    print(data_2)


def team3():
    team_name = data["teams"][2]["teamName"]
    t_z_id = data["teams"][2]["venue"]["timeZone"]["id"]
    abbreviation = data["teams"][2]["abbreviation"]

    data_3 = {
        "Team Name": team_name,
        "TimeZoneID": t_z_id,
        "Abbreviation": abbreviation
    }

    print(data_3)


def team4():
    team_name = data["teams"][3]["teamName"]
    t_z_id = data["teams"][3]["venue"]["timeZone"]["id"]
    abbreviation = data["teams"][3]["abbreviation"]

    data_4 = {
        "Team Name": team_name,
        "TimeZoneID": t_z_id,
        "Abbreviation": abbreviation
    }

    print(data_4)


"""
i have printed data for 4 teams only, because i am lazy enough
you can print all if you wish.
thanks.
"""


team1()
team2()
team3()
team4()
