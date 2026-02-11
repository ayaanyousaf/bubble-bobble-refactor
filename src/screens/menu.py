from src.game import Game

class MenuScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game()

    def update(self, input_state):
        if input_state.fire_pressed:
            # If space is pressed on menu, swithc to play state
            from src.screens.play import PlayScreen
            self.app.change_screen(PlayScreen(self.app))
        else:
            self.game.update(input_state)

    def draw(self, screen):
        self.game.draw(screen)

        screen.blit("title", (0, 0))
        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim_frame), (130, 280))
