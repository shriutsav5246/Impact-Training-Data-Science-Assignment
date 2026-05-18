import csv
from models.match import Match
from models.stadium import Stadium

DATA_FILE = "ipl_project/data/matches.csv"
OUTPUT_FILE = "ipl_project/outputs/match_summary.txt"


def load_matches():
    matches = []

    with open(DATA_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            match = Match(
                team1=row.get("team1", "Unknown"),
                team2=row.get("team2", "Unknown"),
                winner=row.get("winner", "No Result"),
                venue=row.get("venue", "Unknown Stadium"),
                date=row.get("date", "Unknown Date")
            )
            matches.append(match)

    return matches


def save_summary(matches):
    with open(OUTPUT_FILE, mode="w", encoding="utf-8") as file:
        for match in matches[:10]:
            file.write(f"{match.date}: {match.team1} vs {match.team2}\n")
            file.write(f"Winner: {match.winner}\n")
            file.write(f"Venue: {match.venue}\n")
            file.write("-" * 40 + "\n")


def main():
    matches = load_matches()

    print(f"Total Matches Loaded: {len(matches)}")
    print("=" * 50)

    for match in matches[:5]:
        stadium = Stadium(match.venue)
        stadium.display_stadium()
        match.display_match()

    save_summary(matches)

    print("Match summary saved successfully.")


if __name__ == "__main__":
    main()