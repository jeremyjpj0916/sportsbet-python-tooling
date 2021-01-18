import csv
import io
import requests
import classes

if __name__ == '__main__':
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
                                         row[per_dollar_payoutIndex], row[dateIndex], row[american_oddsIndex])
        gamesList.append(tempGame)

    # Print the teams choose as a check from list
    print(gamesList)
