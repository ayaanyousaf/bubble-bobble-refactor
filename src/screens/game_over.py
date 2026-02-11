from src.ui import draw_status

class GameOverScreen: 
    def __init__(self, app, game):
        self.app = app
        self.game = game

    def update(self, input_state):
        if input_state.fire_pressed:
            # If space is pressed on game over screen, switch to menu state
            from src.screens.menu import MenuScreen
            self.app.change_screen(MenuScreen(self.app))

    def draw(self, screen):
        self.game.draw(screen)

        draw_status(self.game, screen)
        
        # Display "Game Over" image
        screen.blit("over", (0, 0))