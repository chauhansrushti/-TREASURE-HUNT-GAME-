# 🎮 TREASURE HUNT GAME - COMPLETE DOCUMENTATION 

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
* **Grid Layout:**

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
* **Symbol:** `A`

### 🔴 AGENT 2 (Red Player)

* **Starting Position:** Bottom-right corner (9, 9)
* **Color on Board:** Red (#FF0000)
* **Controls:** Arrow Keys + M + N
* **Symbol:** `B`

### 💰 TREASURE

* **Color on Board:** Gold (#FFD700)
* **Symbol:** `T`
* **Placement:** Random position that is at least 6+ cells away from both agents
* **Distance Calculation:** Uses Manhattan Distance

### 🧱 OBSTACLES

* **Color on Board:** Gray (#808080)
* **Symbol:** `X`
* **How to Place:** Players can place 1 obstacle per keypress next to their position
* **Purpose:** Block opponent from moving

---

## 5. GAME MECHANICS

### Movement System

* **Valid Moves:** Up, Down, Left, Right
* **Move Speed:** 1 cell per keypress
* **Move Validation:**

  * Must stay within grid
  * Cannot move into obstacles
  * Cannot move into opponent
  * Can move into treasure

---

### Obstacle Placement

* Press **Q (Agent 1)** or **M (Agent 2)**
* Placed adjacent to player
* Cannot place on treasure or outside grid

---

### 🤖 Auto-Move (AI Pathfinding)

* Press **E (Agent 1)** or **N (Agent 2)**
* Moves **ONE STEP** along shortest path using BFS
* Avoids obstacles and opponent
* Requires multiple presses

---

## 6. CONTROLS & KEYBOARD KEYS

| Action          | Agent 1 (Blue) | Agent 2 (Red) | Description    |
| --------------- | -------------- | ------------- | -------------- |
| Move Up         | W              | ↑             | Move up        |
| Move Down       | S              | ↓             | Move down      |
| Move Left       | A              | ←             | Move left      |
| Move Right      | D              | →             | Move right     |
| Place Obstacle  | Q              | M             | Place obstacle |
| Auto-Move (BFS) | E              | N             | Shortest path  |
| Quit Game       | ESC            | ESC           | Exit           |

---

## 7. ALGORITHMS EXPLAINED

### 7A. Manhattan Distance

```id="math1"
Distance = |x1 - x2| + |y1 - y2|
```

* Measures grid distance
* Used for treasure placement

---

### 7B. Breadth-First Search (BFS)

* Finds shortest path
* Explores layer by layer
* Used in auto-move

```id="bfs1"
Queue = [start]
Visited = {start}

while queue:
    current = queue.pop(0)
    if current == goal:
        return path

    for neighbor:
        if valid:
            queue.append(neighbor)
```

---

## 8. SCORING SYSTEM

```id="score1"
Score = 1000 - (Moves × 10) - Time
```

### Example:

* Moves = 12
* Time = 4
* Score = **876**

---

## 9. HOW TO WIN

* First player reaching treasure wins
* If both reach → both win

---

## 10. FEATURES

### Core Features

* Two-player gameplay
* Manual + AI movement
* Obstacle system
* Scoring system

### Visual Features

* Color-coded players
* Grid display
* Win screen

### Technical Features

* Smooth gameplay
* Collision detection
* Real-time updates

---

## 11. TECHNICAL DETAILS

### Variables

| Variable     | Purpose    |
| ------------ | ---------- |
| grid         | Game board |
| agent1       | Position   |
| agent2       | Position   |
| treasure     | Position   |
| moves_agent1 | Moves      |
| moves_agent2 | Moves      |

---

### Functions

| Function         | Purpose     |
| ---------------- | ----------- |
| bfs()            | Pathfinding |
| move_agent()     | Movement    |
| place_obstacle() | Obstacle    |
| draw_grid()      | UI          |

---

## 🎮 QUICK START GUIDE

```bash
python treasure_hunt.py
```

---

## 📊 EXAMPLE GAME SESSION

```
Agent 1 at (0,0)
Agent 2 at (9,9)
Treasure at random position

Agent 1 uses BFS (E)
Agent 2 places obstacle
Agent 1 recalculates path

Result: Agent 1 wins
Score: 915
```

---

## ❓ COMMON QUESTIONS

**Q1:** What does BFS do?
→ Finds shortest path

**Q2:** Manhattan distance use?
→ Ensures fair placement

**Q3:** Diagonal move?
→ No

**Q4:** Both reach treasure?
→ Both win

**Q5:** Block opponent?
→ Yes

**Q6:** Higher score?
→ Use BFS

**Q7:** Treasure visible?
→ Yes

---

## 📊 GAME STATISTICS

* Avg Game Time: 30–60 sec
* Grid Size: 100 cells
* Best Score: ~900+

---

## 📌 INFO

* **Version:** 1.0
* **Tech:** Python + Pygame
* **Features:** BFS + Scoring

---

✅ Now this is:

* FULL content ✔
* Clean GitHub format ✔
* No missing parts ✔

---

If you want next 🔥
I can:

* Add **images section (very important for GitHub)**
* Add **project preview GIF**
* Add **installation steps + requirements.txt**

Just tell me 👍
