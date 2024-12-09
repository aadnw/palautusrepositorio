class All: #tosi kaikille pelaajille
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                continue
        return True

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):

        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def test(self, player):
        for matcher1 in self._matchers:
            for matcher2 in self._matchers:
                if matcher2.test(player):
                    return True
            if matcher1.test(player):
                return True

        return False
    
class Not: #parametrina olevan ehdon negaatio
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return False
            return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan: #HasAtLeast-komennon negaatio eli esim. on vähemmän kuin 10 maalia
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class QueryBuilder:
    def __init__(self, build = All()):
        self.query_build = build

    def plays_in(self, team):
        return QueryBuilder(And(PlaysIn(team), self.query_build))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self.query_build))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self.query_build))
    
    def build(self):
        return self.query_build