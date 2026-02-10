from src.input import space_pressed
from src.ui import draw_status

class GameOverScreen: 
    def __init__(self, app, game):
        self.app = app
        self.game = game

    def update(self):
        if space_pressed():
            # Switch to menu state, and create a new game object without a player
            from src.screens.menu import MenuScreen
            self.app.change_screen(MenuScreen(self.app))

    def draw(self, screen):
        self.game.draw(screen)

        draw_status(self.game, screen)
        
        # Display "Game Over" image
        screen.blit("over", (0, 0))