import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = {}

    for player_dict in response:
        country = player_dict['nationality']
        if country not in players:
            players[country] = ""

    for country in players:
        countrys_players = []
        for player_dict in response:
            if player_dict['nationality'] == country:
                countrys_players.append(Player(player_dict))
        players[country] = countrys_players

    for country in players:
        print("\n"+"Players from "+country+"\n")
        for player in players[country]:
            print(player) 


if __name__ == "__main__":
    main()
