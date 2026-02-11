from src.screens.menu import MenuScreen
from pgzero.builtins import keyboard
from src.input import InputState

class App: 
    def __init__(self):
        self.current_screen = MenuScreen(self)

        self._prev_space = False
        self._prev_jump = False
        self._prev_pause = False

    def change_screen(self, screen): 
        self.current_screen = screen

    def build_input_state(self) -> InputState:
        space_pressed = keyboard.space
        jump_pressed = keyboard.up
        pause_pressed = keyboard.p

        input_state = InputState(
            left=keyboard.left,
            right=keyboard.right,
            jump_pressed=jump_pressed and not self._prev_jump,
            fire_pressed=space_pressed and not self._prev_space,
            fire_held=space_pressed,
            pause_pressed=pause_pressed and not self._prev_pause,
        )

        self._prev_space = space_pressed
        self._prev_jump = jump_pressed
        self._prev_pause = pause_pressed

        return input_state

    def update(self): 
        input_state = self.build_input_state()
        self.current_screen.update(input_state)

    def draw(self, screen): 
        self.current_screen.draw(screen)