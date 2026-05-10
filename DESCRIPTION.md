# Project Description
Echo Knight is a 2D side-scrolling roguelike platformer developed using the Pygame library. Players navigate through a series of dangerous environments, battling a variety of enemies while managing their health and resources.

The project is designed not just as a game, but as a system for analyzing player behavior. By tracking metrics such as survival time and combat efficiency, the system provides insights into how players interact with the game's mechanics and difficulty spikes.

## 1. Project Overview
Provide a high-level understanding of the project.


- **Project Name:**  
  Echo Knight
- **Brief Description:**  
Echo Knight is a combat-oriented platformer where the player controls a knight. The game utilizes a modular class-based architecture to handle physics, entity AI, and UI rendering. It features real-time combat mechanics, including melee and ranged attacks, and tracks detailed gameplay statistics for post-run analysis.

- **Problem Statement:**  
Traditional platformers often lack replayability or fail to provide developers with concrete data on player performance. Echo Knight addresses this by implementing roguelike elements for variety and a dedicated data-logging backend to help understand player difficulty plateaus.

- **Target Users:**  
Players who enjoy challenging, action-oriented roguelikes.

- **Key Features:**  
  - Performance Tracking: A backend system that records every run's stats into a CSV format for visualization.
  - Advanced Enemy AI: Includes various enemy behaviors, such as flying pursuit (Bats), ground-based patrolling (Slimes), and ranged combat (Skeleton Archers).
  - Rougelike Mapping: The platform will be randomized in every new run.

---

## 2. Concept

### 2.1 Background
Echo Knight was born out of a desire to merge the tight, responsive movement of classic side-scrollers with the high-stakes "permadeath" loop of modern roguelikes. It is heavily inspired by Hollow Knight in term of side scrolling, for the atmosphere, I make it feel like a cave dungeon with varius enemies that normally can find in fantasy games. The project serves as an application of Object-Oriented Programming (OOP) principles to solve real-time interaction and state management problems.

### 2.2 Objectives
To implement a robust collision and physics system for a 2D environment.

To create a scalable entity system using inheritance (e.g., different enemy types inheriting from a base class).

To collect and export at least 100 data points of gameplay metrics to analyze player survival patterns.

---

## 3. UML Class Diagram
EchoKnight (Main Class): Aggregates UI, Player, Enemy, and Tile groups. Manages the main game loop.

Entity (Base Class): Handles position and shared physics.

Player & Enemy (Sub-classes): Inherit from a base sprite class; manage health and movement.

StatsManager: Handles the association between game events and CSV file storage.

**Submission Requirement:**  
- Attach the UML Class Diagram in **.pdf format**
![Echo Knight UML Diagram](./Uml_Diagram.pdf)

---

## 4. Object-Oriented Programming Implementation
- **EchoKnight (main.py):** The main controller that manages game states, event handling, and the central loop.
- **Player (entities.py):** Handles physics, animations, health, and combat inputs for the user character.
- **Enemy (entities.py):** A base class for AI entities (Slime, Bat, Skeleton) with unique movement and attack logic.
- **Bullet (entities.py):** Manages the trajectory and damage of player ranged attacks.
- **EnemyArrow (entities.py):** Handles ranged projectiles fired by skeleton enemies.
- **Tile (entities.py):** Represents the static environment and collision blocks.
- **Decoration (entities.py):** Manages non-collidable background visual elements.
- **UI (ui.py):** Handles the rendering of the HUD (Health, Echoes) and menus.
- **Button (ui.py):** A reusable component for interactive menu selection.
- **StatsManager (stats_manager.py):** Collects and exports session data to CSV.

---

## 5. Statistical Data

### 5.1 Data Recording Method
Data is collected in real-time during gameplay through the StatsManager class. Every time a specific event occurs (e.g., an enemy is defeated or the player takes damage), the system appends a row to a game_stats.csv file. This ensures that data is preserved even if the game is closed.

### 5.2 Data Features
1. **Enemies Defeated:** Total count of enemies killed during a run.
2. **Distance Traveled:** Total pixels moved horizontally by the player.
3. **Survival Time:** The total duration of the run in seconds.
4. **Death Cause:** The specific enemy or obstacle that reduced health to zero.

---

## 6. Changed Proposed Features (Optional)
Changed: Transitioned from a top-down perspective (as seen in some inspirations) to a side-scrolling platformer.

Why: To place a higher emphasis on physics-based gameplay, such as gravity and jump timing, which provides more interesting "Distance Traveled" data for analysis.

---

## 7. External Sources
Source Code: Inspired by the framework of VictorHachard/pygame-roguelike (GitHub).

Libraries: - Pygame (Game Engine)

Pandas (Data Processing)

Matplotlib (Visualization)

Artwork: - Custom sprites created using Piskel.

Placeholder backgrounds: - I use AI called Gemini to generate background picture for me.

## 8. Youtube Link
https://youtu.be/ygrWgNIkc2c

