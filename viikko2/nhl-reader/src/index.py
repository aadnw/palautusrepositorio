import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats(PlayerReader):
    def __init__(self, playerreader):
        self.url = playerreader.url

    def top_scores_by_nationality(self, country):
        players = self.get_players()
        players_by_country = []

        for player in players:
            if player.nationality == country:
                players_by_country.append(player)
                players_by_country = sorted(players_by_country, key=lambda player: player.sum)

        print("Players from " + country + "\n")
        return players_by_country
    
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scores_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
