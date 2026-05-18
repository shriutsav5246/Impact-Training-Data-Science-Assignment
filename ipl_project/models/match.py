class Match:
    def __init__(self, team1, team2, winner, venue, date):
        self.team1 = team1
        self.team2 = team2
        self.winner = winner
        self.venue = venue
        self.date = date

    def display_match(self):
        print(f"{self.date}: {self.team1} vs {self.team2}")
        print(f"Winner: {self.winner}")
        print(f"Venue: {self.venue}")
        print("-" * 40)