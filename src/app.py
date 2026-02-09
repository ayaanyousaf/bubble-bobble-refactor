from src.screens.menu import MenuScreen
from src.screens.play import PlayScreen
from src.screens.game_over import GameOverScreen


class App: 
    def __init__(self):
        self.current_screen = MenuScreen(self)

    def update(self): 
        self.current_screen.update()

    def draw(self): 
        self.current_screen.draw()