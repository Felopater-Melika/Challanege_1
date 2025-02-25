import requests
import pandas as pd

print("=== Environment configured...")

url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
csv = "nba.csv"
response = requests.get(url)
response.raise_for_status()

with open(csv, "wb") as f:
    f.write(response.content)
print("=== Download complete...")

df = pd.read_csv("nba.csv")
print("=== DataFrame ready...")

print("\n\n\nTotal Points by NBA Franchise")
print(df.groupby("team_id")["pts"].sum())

print("\n\n\nFinal Game Results for Games 5555 through 5559")
print(df.loc[5555:5559, ["fran_id", "opp_fran", "pts", "opp_pts"]])

print("\n\n\n2015 Warrior W/L Stats:")
print(df[(df["fran_id"] == "Warriors") & (df["year_id"] == 2015)].groupby(["game_result"])["game_id"].count())
