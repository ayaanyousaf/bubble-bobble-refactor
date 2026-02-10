from src.screens.game_over import GameOverScreen
from src.ui import draw_status
from src.game import Game, Player

class PlayScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game(Player())

    def update(self):
        if self.game.player.lives < 0:
            self.game.play_sound("over")
            self.app.change_screen(GameOverScreen(self.app, self.game))
        else:
            self.game.update()

    def draw(self, screen):
        self.game.draw(screen)
        draw_status(self.game, screen)
