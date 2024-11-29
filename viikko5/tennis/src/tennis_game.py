class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.match_score1 = 0
        self.match_score2 = 0
        self.score = ""
        self.temp_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.match_score1 += 1
        else:
            self.match_score2 += 1

    def even_score(self):
        if self.match_score1 == 0:
            self.score = "Love-All"
        elif self.match_score1 == 1:
            self.score = "Fifteen-All"
        elif self.match_score1 == 2:
            self.score = "Thirty-All"
        else:
            self.score = "Deuce"
        return self.score
    
    def score_advantage_or_win(self):
        minus_result = self.match_score1 - self. match_score2

        if minus_result == 1:
            self.score = "Advantage player1"
        elif minus_result == -1:
            self.score = "Advantage player2"
        elif minus_result >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"
        return self.score
    
    def score_regular_points(self):
        for game in range(1, 3):
            if game == 1:
                self.temp_score = self.match_score1
            else:
                self.score += "-"
                self.temp_score = self.match_score2

            if self.temp_score == 0:
                self.score += "Love"
            elif self.temp_score == 1:
                self.score += "Fifteen"
            elif self.temp_score == 2:
                self.score += "Thirty"
            elif self.temp_score == 3:
                self.score += "Forty"
        return self.score


    def get_score(self):
        if self.match_score1 == self.match_score2:
            return self.even_score()

        elif self.match_score1 >= 4 or self.match_score2 >= 4:
            return self.score_advantage_or_win()
    
        else:
            return self.score_regular_points()
            

