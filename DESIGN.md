## Screens Architecture
The updated screen-based architecture involves an App object which owns the current screen and delegates `draw()` and `update()` methods to `main.py`. Each screen has its own class (`MenuScreen`, `PlayScreen`, `GameOverScreen`) which contain their own logic, separated from the rest of the code.

An `app.change_screen()` method is used to handle screen transitions and ensure that `Game()` objects are only created during transitions.

PyGame Zero `screen` is handled globally in the source file and cannot be imported, to work around this, the original screen is passed from `main.py` into App via the `draw(...)` method, which now takes a `screen` argument. This same variable is then passed to all other entities.

## Input Design
Inputs are handled by a centralized `InputState` dataclass. App reads the input using `keyboard` and creates an instance of the `InputState`. This instance is essentially a snapshot containing all possible inputs. The snapshot is then passed on to `Game()` from which the `Player` class can access it.

## Pause Feature
After refactoring the input handling, adding a dedicated pause feature becomes much easier. The pause input `p` is added to the `InputState` and passed only to `PlayScreen` where a boolean flag uses it to track if the game is in a paused state or not. This way, the game can only be paused during gameplay.