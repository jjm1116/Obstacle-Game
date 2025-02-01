Requirements


Software Requirements
  Python 3.x - The game is written in Python and requires Python 3.x or higher.
  Pygame - The game uses the Pygame library for game development, specifically for graphics rendering, event handling, and user input.
  To install Pygame, use the following command:
    pip install pygame

Hardware Requirements
  Operating System: The game is compatible with Windows, macOS, and Linux (any platform that supports Pygame).
  RAM: At least 1 GB of system memory.
  CPU: Any modern processor should suffice.
  Graphics: Any basic graphics card that supports windowed mode rendering.
  Display: The game runs at a resolution of 600x400 pixels.


Game Mechanics
  Player Character:
    The player is represented as a blue circle with a radius of 25 pixels.
    The player can move using the arrow keys (Up, Down, Left, Right) or WASD keys.
    The player can move around the screen with a speed of 10 pixels per frame.

Obstacles:
  Obstacles are randomly placed rectangles (50x50 pixels).
  The number of obstacles increases as the player progresses through stages.

Target:
  The target is a randomly placed red rectangle (50x50 pixels).
  The player must reach the target to advance to the next stage.

Stages:
  The game consists of multiple stages, each with a unique difficulty setting.
    Each stage has:
      A number of obstacles (which increases as the stages get harder).
      A time limit (in milliseconds) that decreases as the stages progress.
    The stages are as follows:
      Easy (3 obstacles, 60,000 ms time limit)
      Medium (4 obstacles, 50,000 ms time limit)
      Hard (5 obstacles, 40,000 ms time limit)
      Insane (6 obstacles, 30,000 ms time limit)
      Expert (7 obstacles, 20,000 ms time limit)
      Mad (8 obstacles, 15,000 ms time limit)
      Shenanigans (8 obstacles, 13,000 ms time limit)
      Crazy (8 obstacles, 10,000 ms time limit)
      Final Exam (8 obstacles, 8,000 ms time limit)
      Asian (9 obstacles, 5,000 ms time limit)
      ??? (10 obstacles, 4,000 ms time limit)

Grace Period:
  The player has a grace period during which they are immune to collisions with obstacles.
  The grace period is set to 600 ms and decreases over time.
  If the player collides with an obstacle outside of the grace period, they lose the game.

Time Limit:
  Each stage has a countdown timer that limits how long the player has to reach the target.
  If the timer reaches 0 before the player reaches the target, the game ends.

Game End Conditions:
  Win Condition: The player reaches the target before the time runs out and progresses to the next stage.
  Lose Condition: The player collides with an obstacle or runs out of time.

End Screen:
  When the game ends, a screen is displayed offering two options:
  Replay: Restart the game from the first stage.
  Quit: Exit the game.
  User Interface

Main Screen:
  The main game screen displays:
  The player's position (blue circle).
  The target (red rectangle).
  The obstacles (black rectangles).
  The current stage number and name (e.g., "Stage 1 (Easy)").
  The remaining time in seconds.
  The background is white.
  The player's movement is smooth and responsive, limited by the screen boundaries.

End Screen:
  Upon game over or completion of the final stage, an end screen appears.
  The screen displays:
  A message ("You Win!", "Game Over!", "Time's Up!") based on the game result.
  Two options:
  Replay: Restarts the game from the first stage.
  Quit: Exits the game.



Code Details

Main Game Loop:
  The game runs within a continuous loop, processing player input, updating positions, checking for collisions, and rendering the scene.

Player Movement:
  Player movement is handled by checking for key presses and updating the player's position based on those inputs.
  Movement is confined within the screen boundaries (600x400).

Collision Detection:
  The game checks for collisions between the player and the target, the player and obstacles, and the player and the screen boundaries.
  When the player collides with an obstacle, the game enters the end screen.

Timer Logic:
  The stage timer and grace period timer decrease over time.
  If the stage timer reaches zero, the game ends with a "Time's up!" message.
  If the player reaches the target, they progress to the next stage and the timer resets.

Obstacles Generation:
  Obstacles are generated randomly for each stage and are placed in non-overlapping positions with respect to the player and target.

Grace Period:
  The grace period is visualized by an aura around the player that fades as time passes.



Additional Notes
  The game uses randomization for obstacle placement and target positioning, ensuring that each playthrough offers a unique challenge.
  The time limit for each stage is designed to gradually become more difficult as the player progresses through the game.
  The grace period adds an element of strategy, allowing the player to take risks early in each stage.
