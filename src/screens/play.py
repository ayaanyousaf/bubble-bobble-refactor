from src.screens.game_over import GameOverScreen
from src.ui import draw_status
from src.game import Game, Player

class PlayScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game(Player())
        self.paused = False

    def update(self, input_state):
        # Change pause state if pause button is pressed
        if input_state.pause_pressed:
            self.paused = not self.paused
            return 
        
        # Freeze the game if paused state is active
        if self.paused:
            return

        if self.game.player.lives < 0:
            self.game.play_sound("over")
            self.app.change_screen(GameOverScreen(self.app, self.game))
        else:
            self.game.update(input_state)

    def draw(self, screen):
        self.game.draw(screen)
        draw_status(self.game, screen)
