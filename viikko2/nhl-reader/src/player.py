class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
        self.games = dict['games']
        self.id = dict['id']

        self.sum = self.goals+self.assists
    
    def __repr__(self):
        return f"{self.name:20} team {self.team:10} {self.goals:} + {self.assists:} = {self.sum}"
