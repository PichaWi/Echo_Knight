# Echo Knight

## Project Description

- Project by: Picha Wiwattanawongsa
- Game Genre: Action, Side scrolling

Echo Knight is a 2D side-scrolling roguelike platformer developed using the Pygame library. Inspired by the atmosphere and tight mechanics of games like Hollow Knight, players take on the role of a knight navigating through dungeon cave environments.

The project emphasizes fluid movement and high-stakes combat. Every playthrough is unique due to random platform spawned and each different run and the game integrates a data-tracking system that records player performance—such as survival time and combat effectiveness—into a CSV file for post-game analysis.

---

## Installation
To Clone this project:
```sh
git clone https://github.com/PichaWi/Year_project.git
```

To create and run Python Environment for This project:

Window:
```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Mac:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Running Guide
After activate Python Environment of this project, you can process to run the game by:

Window:
```bat
python main.py
```

Mac:
```sh
python3 main.py
```

---

## Tutorial / Usage
Movement: Use A to move left and D to move right.

Jumping: Press Space to jump.

Melee Attack: Press Left Click to perform a sword slash. This deals damage and provides a slight knockback to enemies.

Ranged Attack: Press Right Click to fire a laser projectile. Note that there is a cooldown between shots.

Goal: Traverse the map and defeat enemies to progress. If your health reaches zero, the "Echo" ends, and your stats are automatically logged.

---

## Game Features
Dynamic Physics: Implementation of real-time gravity and acceleration for fluid platforming.

Automated Stats Logging: Uses a StatsManager to record run-time data including survival duration, distance traveled, and specific causes of death.

Enemy Variety: Different enemy types including Slimes, Bats, and Skeletons (Sword and Bow variants) with unique behaviors.

Animation System: Animated sprites created with Piskel.

---

## Known Bugs
Tile Collision Jitter: The player may occasionally exhibit small jitters when jumping directly against the corner of a wall tile.

Projectile Edge Case: If a projectile is fired at the exact moment a scene transitions, it may occasionally fail to despawn.

Image might not generated, please make sure you provide correctly file location if can't run in your device.

---

## Unfinished Works
Permanent Upgrades: The logic for a persistent skill tree using collected "Echoes" is planned but currently only exists as a session-based score.

Boss Battles: While standard enemies are fully implemented, the final boss encounter for the cave depths is still in the design phase.

Other: There many content I already finished but lose due to changing device of myself, making what current game now are unfinished version of what I have done.

---

## External sources
Acknowledge to:
1. VictorHachard/pygame-roguelike: Foundation for the tile-based world logic and roguelike structures.

2. Pygame Community: Documentation and tutorials for handling sprite collisions and mask-based physics.

3. Piskel App: Tool used for all original 2D pixel art and frame-by-frame animations.
