from src.game import Game, Player
from src.input import space_pressed

class MenuScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game()

    def update(self):
        if space_pressed():
            from src.screens.play import PlayScreen
            self.app.change_screen(PlayScreen(self.app))
        else:
            self.game.update()

    def draw(self, screen):
        self.game.draw(screen)

        screen.blit("title", (0, 0))
        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim_frame), (130, 280))
