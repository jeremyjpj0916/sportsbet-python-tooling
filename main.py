import csv
import io
import requests
import classes
from pysbr import *
from datetime import datetime

if __name__ == '__main__':

    ### First portion, scrape all games we want to bet on ###

    url = 'https://raw.githubusercontent.com/axz2000/sportsbook/main/masterScript/masterPush.csv'
    response = requests.get(url)
    csv_bytes = response.content
    str_file = io.StringIO(csv_bytes.decode('utf-8'), newline='\n')
    csvReader = csv.reader(str_file)

    header = next(csvReader)
    teamChosenIndex = header.index("Bet State Chosen")
    percentageIndex = header.index("Allocation Percentage")
    leagueIndex = header.index("League")
    per_dollar_payoutIndex = header.index("Payouts (per Dollar)")
    dateIndex = header.index("Date")
    american_oddsIndex = header.index("American Odds")
    # Make an empty games list
    gamesList = []

    # Loop through the lines in the file and get each element we want for sportsbetgame object and add it to the list of games.
    for row in csvReader:
        tempGame = classes.SportsBetGame(row[teamChosenIndex], row[percentageIndex], row[leagueIndex],
                                         row[per_dollar_payoutIndex], row[dateIndex], row[american_oddsIndex], "", "")
        gamesList.append(tempGame)

    ### Second portion, check if games we want to bet on exist at favorable odds with bookies ###

    ### Configurable variables ###

    # Example options found here: https://github.com/JeMorriso/PySBR/blob/main/pysbr/config/sportsbooks.yaml
    bookie_list = ['BetOnline', 'Bovada']
    game_type = ['moneyline']

    ### END OF Configurable variables ###

    dt = datetime.strptime(datetime.today().strftime('%Y-%m-%d'), '%Y-%m-%d')
    nfl = NFL()
    nba = NBA()
    sb = Sportsbook()
    e_nfl = EventsByDate(nfl.league_id, dt)
    e_nba = EventsByDate(nba.league_id, dt)
    cl_nfl = CurrentLines(e_nfl.ids(), nfl.market_ids(game_type), sb.ids(bookie_list))
    cl_nba = CurrentLines(e_nba.ids(), nba.market_ids(game_type), sb.ids(bookie_list))

    for game in gamesList:
        if game.league == "KHL":
            print("KHL LEAGUE GAME PROCESSING")
            print(game)
        elif game.league == "NHL":
            print("NHL LEAGUE GAME PROCESSING")
            print(game)
        elif game.league == "NFL":
            print("NFL LEAGUE GAME PROCESSING")
            for match in cl_nfl.list(e_nfl):
                if match['event'].lower().find(str(game.team_chosen).lower()):  # match found
                    if match['american odds'] >= int(game.american_odds):
                        if isinstance(game.bookie_odds, int):  # If another bookie has better value replace again
                            if match['american odds'] > game.bookie_odds:
                                game.bookie = match['sportsbook']
                                game.bookie_odds = match['american odds']
                        else:
                            game.bookie = match['sportsbook']
                            game.bookie_odds = match['american odds']
        elif game.league == "NBA":
            print("NBA LEAGUE GAME PROCESSING")
            for match in cl_nba.list(e_nba):
                if match['event'].lower().find(str(game.team_chosen).lower()):  # match found
                    if match['american odds'] >= int(game.american_odds):
                        if isinstance(game.bookie_odds, int):  # If another bookie has better value replace again
                            if match['american odds'] > game.bookie_odds:
                                game.bookie = match['sportsbook']
                                game.bookie_odds = match['american odds']
                        else:
                            game.bookie = match['sportsbook']
                            game.bookie_odds = match['american odds']
        elif game.league == "LLA":
            print("LLA LEAGUE GAME PROCESSING")
            print(game)
        elif game.league == "PPL":
            print("PPL LEAGUE GAME PROCESSING")
            print(game)
        elif game.league == "ELO":
            print("ELO LEAGUE GAME PROCESSING")
            print(game)
        elif game.league == "EPL":
            print("EPL LEAGUE GAME PROCESSING")
            print(game)
        elif game.league == "GPL":
            print("GPL LEAGUE GAME PROCESSING")
            print(game)
        elif game.league == "ISA":
            print("ISA LEAGUE GAME PROCESSING")
            print(game)
        elif game.league == "TSL":
            print("TSL LEAGUE GAME PROCESSING")
            print(game)
        elif game.league == "NPL":
            print("NPL LEAGUE GAME PROCESSING")
            print(game)
        elif game.league == "FL1":
            print("FL1 LEAGUE GAME PROCESSING")
            print(game)
        elif game.league == "BPL":
            print("BPL LEAGUE GAME PROCESSING")
            print(game)

    # Print the games list as a test.
    print(gamesList)
