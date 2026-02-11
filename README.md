# Refactoring PyGame Zero Bubble Bobble Clone
##### Author: Ayaan Yousaf

--- 

Source Code: https://github.com/Wireframe-Magazine/Code-the-Classics/tree/master/cavern-master

## Running the Game
1. Clone the repository
2. Run main.py through your IDE or terminal: 
    ```bash
    pgzrun main.py
    ```

## Architectural Changes
- Global state branching has been replaced by an App object that manages the current screen, and screen transitions for each screen (Menu, Play, Game Over). Each screen has an object that implements its own `draw()` and `update()` methods.

- A centralized input state with edge detection has been added to handle all inputs across all screens instead of entities accessing `keyboard` independently.

- Pause feature implemented in the Play screen using the input state. The screen uses a boolean flag to track pause state, and the game can only be paused during gameplay.
