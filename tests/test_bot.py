import unittest
from src.bot import EducationalChatbot

class TestEducationalChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = EducationalChatbot()

    def test_greeting(self):
        self.assertIn(self.bot.respond("Hello"), ["Hello!", "Hi there!", "Greetings!"])

    def test_unknown_input(self):
        self.assertEqual(self.bot.respond("What is quantum computing?"), "Sorry, I don't understand that.")

if __name__ == "__main__":
    unittest.main()
