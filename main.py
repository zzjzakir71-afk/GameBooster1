from kivy.app import App
from kivy.uix.label import Label

class GameBooster(App):
    def build(self):
        return Label(text="🔥 Game Booster App Running")

GameBooster().run()
