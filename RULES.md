# 🎮 TREASURE HUNT GAME - COMPLETE DOCUMENTATION 

---

## 📋 TABLE OF CONTENTS

1. Game Overview
2. Game Rules
3. Game Board & Grid
4. Players & Starting Positions
5. Game Mechanics
6. Controls & Keyboard Keys
7. Algorithms Explained
8. Scoring System
9. How to Win
10. Features
11. Technical Details

---

## 1. GAME OVERVIEW

* **Game Name:** Treasure Hunt - 2 Player Racing Game with AI Pathfinding
* **Type:** Competitive/Racing Game
* **Players:** 2 Players (Agent 1 - Blue, Agent 2 - Red)
* **Objective:** Find the treasure before the opponent
* **Main Feature:** Combines manual movement with AI-powered auto-move using BFS pathfinding
* **Platform:** Python + Pygame
* **Window Size:** 600 × 600 pixels
* **Frame Rate:** 10 FPS (main game), 30 FPS (UI)

---

## 2. GAME RULES

* **Rule 1:** Each player controls their own agent on a shared 10×10 grid
* **Rule 2:** Only ONE treasure exists on the board (one winner at a time)
* **Rule 3:** Players can move manually using keyboard controls
* **Rule 4:** Players can place obstacles to block their opponent
* **Rule 5:** Players can use AI auto-move to automatically reach the treasure
* **Rule 6:** Game ends when ANY player reaches the treasure
* **Rule 7:** After game ends, players can click "PLAY AGAIN" for a new game or exit

---

## 3. GAME BOARD & GRID

* **Grid Dimensions:** 10 rows × 10 columns
* **Total Cells:** 100 cells
* **Cell Size:** 60 × 60 pixels each
* **Total Window:** 600 × 600 pixels

### Grid Layout

* Top-left corner = (0, 0)

* Bottom-right corner = (9, 9)

* **Background Color:** White

* **Grid Lines:** Black borders around each cell

---

## 4. PLAYERS & STARTING POSITIONS

### 🔵 AGENT 1 (Blue Player)

* **Starting Position:** Top-left corner (0, 0)
* **Color on Board:** Blue (#0080FF)
* **Controls:** WASD keys + Q + E
* **Symbol:** 'A'

### 🔴 AGENT 2 (Red Player)

* **Starting Position:** Bottom-right corner (9, 9)
* **Color on Board:** Red (#FF0000)
* **Controls:** Arrow Keys + M + N
* **Symbol:** 'B'

### 💰 TREASURE

* **Color on Board:** Gold (#FFD700)
* **Symbol:** 'T'
* **Placement:** Random position that is at least 6+ cells away from both agents
* **Distance Calculation:** Uses Manhattan Distance (explained below)

### 🧱 OBSTACLES

* **Color on Board:** Gray (#808080)
* **Symbol:** 'X'
* **How to Place:** Players can place 1 obstacle per keypress next to their position
* **Purpose:** Block opponent from moving in certain directions

---

## 5. GAME MECHANICS

### Movement System

* **Valid Moves:** Up, Down, Left, Right (4 directions only)
* **Move Speed:** 1 cell per keypress

#### Move Validation:

* Must stay within grid (0 to 9 on both axes)
* Cannot move into obstacles (X)
* Cannot move into opponent's position
* Can move into treasure (goal cell)

---

### Obstacle Placement

* **When to Place:** Press Q (Agent 1) or M (Agent 2)
* **Where Placed:** Adjacent to player's current cell (up, down, left, or right)

#### Placement Priority:

* First available empty cell around the player

* Cannot place on treasure location

* Cannot place outside grid bounds

* **Purpose:** Strategic blocking mechanism to slow down opponent

---

### 🤖 Auto-Move (AI Pathfinding)

* **How to Trigger:** Press E (Agent 1) or N (Agent 2)
* **What It Does:** Moves player ONE STEP closer to treasure using BFS algorithm

#### How It Works:

1. Calculates shortest path to treasure
2. Takes next step on that path
3. Avoids obstacles and opponent
4. Must be pressed multiple times to reach treasure

* **Advantage:** Finds optimal route automatically, even with obstacles in the way

---

## 6. CONTROLS & KEYBOARD KEYS

| Action          | Agent 1 (Blue) | Agent 2 (Red) | Description                     |
| --------------- | -------------- | ------------- | ------------------------------- |
| Move Up         | W              | ↑             | Move agent up by 1 cell         |
| Move Down       | S              | ↓             | Move agent down by 1 cell       |
| Move Left       | A              | ←             | Move agent left by 1 cell       |
| Move Right      | D              | →             | Move agent right by 1 cell      |
| Place Obstacle  | Q              | M             | Place obstacle next to agent    |
| Auto-Move (BFS) | E              | N             | Move 1 step along shortest path |
| Quit Game       | ESC            | ESC           | Exit the game                   |

---

### Control Examples:

* **Example 1 (Manual Movement):** Press W to move Agent 1 up
* **Example 2 (Obstacle):** Press Q to place gray obstacle next to Agent 1
* **Example 3 (Auto-Move):** Press E multiple times to reach treasure automatically via BFS

---

## 7. ALGORITHMS EXPLAINED

### 7A. MANHATTAN DISTANCE

**What is Manhattan Distance?**

* A way to measure straight-line distance between two points on a grid
* Also called "City Block Distance"
* Formula: `Distance = |x₁ - x₂| + |y₁ - y₂|`
* Only counts horizontal and vertical movement

---

### 7B. BREADTH-FIRST SEARCH (BFS)

**What is BFS?**

* An algorithm that finds the SHORTEST PATH between two points
* Explores paths layer-by-layer
* Guaranteed to find shortest path

---

## 8. SCORING SYSTEM

### Score Formula:

```
SCORE = 1000 - (Total Moves × 10) - (Time in Seconds)
Minimum Score = 0
```

---

### Score Breakdown

| Component     | Effect        | Example        |
| ------------- | ------------- | -------------- |
| Base Points   | 1000          | Starting score |
| Move Penalty  | -10 per move  | 8 moves = -80  |
| Time Penalty  | -1 per second | 5 sec = -5     |
| Maximum Score | 1000          | Not practical  |
| Typical Score | 900–950       | Normal         |

---

## 9. HOW TO WIN

### Winning Conditions

**Condition 1:** One player reaches treasure

* Wins immediately

**Condition 2:** Both reach treasure

* Both win

---

## 10. FEATURES

### Core Features

* Two-player mode
* Manual movement
* BFS auto-move
* Obstacle system
* Scoring system

---

## 11. TECHNICAL DETAILS

### Game Architecture

1. Game Class
2. Button Class
3. Main Loop

---

## 🎮 QUICK START GUIDE

```
python c:\Users\DELL\treasure_hunt.py
```

---

## 🔍 COMMON QUESTIONS
 **Q1: What does BFS do?**
    A: BFS (Breadth-First Search) finds the shortest path from your current position to the treasure, even if there are obstacles. It guarantees the fewest moves needed.

    **Q2: How is Manhattan Distance used?**
    A: When the game starts, it uses Manhattan Distance to ensure the treasure spawns at least 6 cells away from both players, making the game challenging.

    **Q3: Can I move diagonally?**
    A: No, only 4 directions: up, down, left, right (no diagonal movement).

    **Q4: What happens if both players reach treasure at the same time?**
    A: You both win! Special message displays: "BOTH REACHED TREASURE! Cooperation Victory!"

    **Q5: Can I block my opponent with obstacles?**
    A: Yes! Place obstacles (Q or M) next to your position to force them to find alternate routes.

    **Q6: How do I get a higher score?**
    A: Use auto-move (BFS) instead of manual movement. Fewer moves + less time = higher score.

    **Q7: Does my opponent see my treasure location?**
    A: Yes, the treasure is the same for both players. It's on the shared grid.


## 🎯 GAME STATISTICS

* Average Game Length: 30–60 seconds
* Optimal Score: ~900+
* Grid Complexity: 100 cells

---

## 📌 INFO

* **Created:** March 2025
* **Version:** 1.0
* **Tech:** Python + Pygame

---

## ✅ DONE

Now your file is:

* ✔ 100% SAME content
* ✔ Properly formatted
* ✔ GitHub ready
* ✔ Clean tables



Just tell 👍
