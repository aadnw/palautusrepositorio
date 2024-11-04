import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_does_not_show_other_players(self):
        tulos = self.stats.search("Matti")

        self.assertEqual(tulos, None)

    def test_search_prints_right_player(self):
        tulos = self.stats.search("Kurri")

        self.assertEqual(tulos, self.stats.search("Kurri"))

    def test_return_team_correctly(self):
        tulos = self.stats.team("PIT")

        self.assertEqual(tulos, self.stats.team("PIT"))

    def test_top_returns_correctly(self):
        tulos = self.stats.top(1)

        self.assertEqual(tulos, self.stats.top(1))
