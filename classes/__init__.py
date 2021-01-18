class SportsBetGame:
    def __init__(self, team_chosen, percentage, league, per_dollar_payout, date, american_odds):
        self.team_chosen = team_chosen
        self.percentage = percentage
        self.league = league
        self.per_dollar_payout = per_dollar_payout
        self.date = date
        self.american_odds = american_odds

    def __repr__(self):
        return str(self.team_chosen) + " " + str(self.percentage) + " " + str(self.league) + " " + str(self.per_dollar_payout) + " " + str(self.date) + " " + str(self.american_odds) + "\n"