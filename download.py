import argparse
import requests
import csv
from datetime import datetime

LOGIN_ENDPOINT = "https://play.topgolf.com/api/auth"
GAMES_ENDPOINT = "https://play.topgolf.com/api/member/games?react"

# Arg parse
parser = argparse.ArgumentParser(description="Fetch your TopGolf data")
parser.add_argument('email', type=str)
parser.add_argument("password", type=str)
args = parser.parse_args()

s = requests.Session()
# POST login
login_details = {"email": args.email, "password": args.password}
login_request = s.post(LOGIN_ENDPOINT, data=login_details)
# TODO: Check that login worked

# Open CSV output
file = open('output.csv', 'w', newline='')
output = csv.writer(file)
# Header labels
output.writerow(["Game ID", "Bay", "Location", "Time", "Game Type", "Ball Order", "Points", "IsBonus", "IsDouble", "IsEdited", "IsHoleInOne", "IsNotRegistered"])

# Fetch the games
game_request = s.get("https://play.topgolf.com/api/member/games?react")
# TODO: error handling
# Response is JSON.
games = game_request.json()['data']['Games']
# Loop through each game
for game in games:
    # Parse date and time to datetime object for later formatting
    dt = datetime.strptime("{} {}".format(game['Date'], game['Time']), "%d/%m/%y %H:%M")
    # Loop through each ball (for player 0)
    # Note that only balls were points were scored are included
    # Define a range of 1-20,
    for ball in game['Players'][0]['Balls']:
        output.writerow([
            game['GameId'],
            game['Bay'],
            game['Location'],
            dt.isoformat(),
            game['GameType'],
            ball['BallOrder'],
            ball['Points'],
            1 if ball['IsBonus'] else 0,
            1 if ball['IsDouble'] else 0,
            1 if ball['IsEdited'] else 0,
            1 if ball['IsHoleInOne'] else 0,
            1 if ball['IsNotRegistered'] else 0
        ])