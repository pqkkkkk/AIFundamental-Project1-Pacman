# Pacman AI Game - project of the Introduction to Artificial Intelligence course

This project is a Pacman game implemented in Python using Pygame, featuring AI-controlled ghosts that use various search algorithms (BFS, DFS, UCS, A*) to chase Pacman. The game includes multiple levels, each demonstrating different AI behaviors and performance statistics.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Game Levels](#game-levels)
- [Project Structure](#project-structure)
- [Search Algorithms](#search-algorithms)
- [Notes](#notes)

---

## Features

- Playable Pacman game with classic mechanics.
- Four search algorithms for ghost AI: BFS, DFS, UCS, and A*.
- Six levels, including both static and dynamic Pacman scenarios.
- Performance statistics (nodes expanded, time, memory) shown after each game.
- Automatic GIF export of gameplay for levels 1–4.
- Modular code structure for easy extension.

## Requirements

- Python 3.10 or higher
- Packages: `pygame`, `imageio`, `psutil`

## Installation

1. **Install Python:**  
   Download and install Python from [python.org](https://www.python.org/).

2. **Install dependencies:**  
   Open a terminal in the `Submission/Source` directory and run:
   ```sh
   pip install -r requirements.txt
   ```

## How to Run

1. Change directory to `Submission/Source`:
   ```sh
   cd Submission/Source
   ```

2. Run the game:
   ```sh
   python main.py
   ```
   or
   ```sh
   py main.py
   ```

3. Select a level by pressing keys 1–6 in the level selection window.

## Game Levels

- **Level 1–4:**  
  Each level demonstrates a different search algorithm for the ghost:
  - Level 1: BFS (Blue Ghost)
  - Level 2: DFS (Pink Ghost)
  - Level 3: UCS (Orange Ghost)
  - Level 4: A* (Red Ghost)  
  After Pacman is caught, the game displays the number of expanded nodes, time spent, and memory usage.

- **Level 5:**  
  Pacman is stationary. Four ghosts, each using a different algorithm, chase Pacman. The game ends when Pacman is caught, displaying which ghost caught Pacman and the elapsed time.

- **Level 6:**  
  Pacman can move. Four ghosts, each using a different algorithm, chase Pacman. The game ends when Pacman is caught, displaying which ghost caught Pacman and the score.

## Project Structure

```
Project1/
│
├── .gitignore
├── README.md
└── Submission/
    └── Source/
        ├── Events.py
        ├── Global.py
        ├── main.py
        ├── README.txt
        ├── requirements.txt
        ├── SearchAlgorithms.py
        ├── frames/
        ├── game_options/
        │   ├── Level1To4.py
        │   ├── Level5.py
        │   └── Level6.py
        ├── images/
        │   ├── BlueGhost.png
        │   ├── Coin.png
        │   ├── OrangeGhost.png
        │   ├── pacman_beginning.wav
        │   ├── Pacman.png
        │   ├── PinkGhost.png
        │   └── RedGhost.png
        └── objects/
            ├── Coin.py
            ├── EventManager.py
            ├── Ghost.py
            ├── Pacman.py
            └── ScoreManager.py
```

## Search Algorithms

The ghost AI uses the following algorithms, implemented in [`SearchAlgorithms.py`](Submission/Source/SearchAlgorithms.py):

- **BFS (Breadth-First Search):** Finds the shortest path by exploring all neighbors at the current depth before moving to the next level.
- **DFS (Depth-First Search):** Explores as far as possible along each branch before backtracking.
- **UCS (Uniform Cost Search):** Expands the node with the lowest path cost.
- **A\* (A-Star):** Uses a heuristic (Manhattan distance) to find the optimal path efficiently.

## Notes

- Make sure all assets (images, sounds) are present in the `images` folder.
- If you encounter issues, ensure your working directory is set to `Submission/Source`.
- For best results, use a Python virtual environment.
- Gameplay frames for levels 1–4 are saved and exported as GIFs for demonstration.

---

**Authors:**  
- Intro to Artificial Intelligence - Pacman AI Project  
- University of Information Technology
