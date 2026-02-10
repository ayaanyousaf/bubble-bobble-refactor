from src.screens.menu import MenuScreen

class App: 
    def __init__(self):
        self.current_screen = MenuScreen(self)

    def change_screen(self, screen): 
        self.current_screen = screen

    def update(self): 
        self.current_screen.update()

    def draw(self, screen): 
        self.current_screen.draw(screen)