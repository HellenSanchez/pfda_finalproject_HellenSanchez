# pfda_finalproject_HellenSanchez
Final Project for PFDA class

# Car Race Dodge

## Demo
Demo Video:

## GitHub Repository
GitHub Repo: https://github.com/HellenSanchez/pfda_finalproject_HellenSanchez.git

## Description
Car Race Dodge is a Python game where the player controls a car to avoid falling traffic cones while driving through a scrolling environment with trees, grass, and lane lines. This project combines programming with digital art and media, using custom pixel art graphics and smooth animations to create an engaging interactive experience.

## Features
- **Car Movement**
The player can move the car horizontally across the road using keyboard inputs (left and right arrows).

- **Falling Cones/Obstacles**
Traffic cones fall from the top of the screen at a constant speed. After score 20, their speed increases. Cones respawn above the screen for continuous gameplay.

- **Scoring System**
  The score increases every time the player successfully avoids cones and is displayed above the obstacles in real-time.

- **Collision and Restart**
When the car hits a cone, a message “Oops! You hit a cone” appears.  
The player can restart by pressing **SPACE** or quit the game by pressing **ESC**.

- **Scrolling Environment**
Trees, grass, and lane lines move downward smoothly to simulate driving. Cones are drawn behind the trees for correct layering.

- **Custom Graphics**
The car, cone, and tree images used in the game are custom PNGs prepared and scaled to match the pixel art style.

## Challenges
- Learning Pygame for animation, input handling, and collision detection.
- Implementing an efficient collision detection system between the car and cones.
- Creating a scoring system that updates in real-time.
- Designing pixel art graphics for cars, cones, and trees.
- Implementing smooth movement for environment elements without "teleporting" visuals.

## Outcomes
**Ideal Outcome:**
A fully functional game with smooth movement, accurate collision detection, continuous obstacles, visible scoring, and an “Oops! You hit a cone” screen allowing restart or quit.

**Minimal Viable Outcome:**
A playable game where the car can move left/right, cones fall, the score increases when avoiding cones, and the game restarts automatically on collision.

## Future Improvements
- Include background music and sound effects for a more immersive experience.
- Add levels or increasing difficulty to extend gameplay. 
- Add multiple car skins and obstacle types for variety.  

## Files in Repository
- **src/project.py** – Main game code with all functions and classes.  
- **src/*.png** – PNG images used in the game (car, cone, tree).  
- **proposal.md** – Project proposal submitted for the course.
- **README.md** – This file with project description, demo link, and instructions.  
- **requirements.txt** – Lists Python libraries required (`pygame`).  