# Car Race Dodge

## Repository
[Car Race Dodge GitHub Repository Link](https://github.com/HellenSanchez/pfda_finalproject_HellenSanchez.git)

## Description
A racing game in Python where the player controls a car to avoid falling cones while driving through a scrolling environment with trees, grass, and lane lines.

## Features
- Feature 1
  - The player can move the car horizontally across the road to avoid obstacles. 
  - Movement is controlled using keyboard inputs detected by Pygame.
- Feature 2
  - Traffic cones fall from the top of the screen at a constant speed (increasing after score 20). 
  - Cones respawn above the screen to create continuous obstacles.
- Feature 3
  - Scoring System: Each time the car successfully avoids cones, the score increases and is displayed above the cones.
  - Implemented using a score variable that is rendered on the screen.
- Feature 4
  - Collision and Restart: When the car hits a cone, the game shows an overlay that says: "Oops! You hit a cone." 
  - The player can restart by pressing SPACE or quit the game by pressing ESC.
- Feature 5
  - Trees, grass, and lane lines move downward smoothly to simulate the illusion of driving. 
  - Cones are drawn behind the trees for correct layering.
- Feature 6
  - The graphics of cars, cones, and trees are custom PNG images created by me, uploaded to the game, and scaled to match the pixel art aesthetic.

 
## Challenges
- Learn to use Pygame for animation and keyboard input handling.
- Learn to create an efficient collision detection system between the car and cones.
- Learn to implement a scoring system that updates and displays in real-time.
- Research/learn to design the car and cone graphics using pixel art.
- Implementing smooth movement for trees, grass, and road lines to avoid “teleporting” visuals.

## Outcomes
Ideal Outcome:
- A fully functional game with smooth movement, accurate collision detection, obstacles spawning continuously, visible scoring, and an “Oops! You hit a cone” screen that allows the player to restart the game by pressing SPACE or quit by pressing ESC.

Minimal Viable Outcome:
- A game where the car can move left and right, cones fall, the score increases when avoiding cones, and the game restarts automatically upon collision.

## Milestones

- Week 1
  1. Goal 1: Create the public GitHub repository.
  2. Goal 2: Create the 'Proposal.md' file and write the full proposal.

- Week 2
  1. Goal 1: Implement car movement left and right.
  2. Goal 2: Design car, cone, and tree graphics (As PNGs) and initialize the game screen to display them.

- Week 3
  1. Goal 1: Implement cones falling from the top and collision detection.
  2. Goal 2: Implement scoring system that updates in real-time and display score on the screen.

- Week 4 (Final)
  1. Goal 1: Add the final "Oops! You hit a cone" screen with options to restart (SPACE) or quit (ESC.)
  2. Goal 2: Polish visuals and animations, finalize features, test the game, record the demonstration video, update the README.md, and submit the project on GitHub and eLearning.
