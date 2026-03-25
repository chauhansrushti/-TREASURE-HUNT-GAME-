# ============================================================
# TREASURE HUNT GAME - 2 Player Racing Game with AI Pathfinding
# ============================================================
# Players race to find treasure on a 10x10 grid
# Use manual controls or BFS auto-move (AI pathfinding)
# ============================================================

import pygame  # Graphics library
import random  # Random treasure placement
import time    # Game timing & scoring
from collections import deque  # For BFS queue

# ============= GAME CONSTANTS =============
GRID_SIZE = 10          # 10x10 grid
CELL_SIZE = 60          # 60x60 pixels per cell
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE  # 600x600 window
FPS = 10                # 10 frames per second
MIN_TREASURE_DIST = 6   # Treasure must be 6+ cells from agents
FONT_SIZE = 30
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50 
 
# ============= COLORS (RGB Format) =============
WHITE = (255, 255, 255)          # Background
BLACK = (0, 0, 0)                # Grid lines
TREASURE_COLOR = (255, 215, 0)    # Gold treasure
AGENT1_COLOR = (0, 128, 255)      # Blue player
AGENT2_COLOR = (255, 0, 0)        # Red player
OBSTACLE_COLOR = (128, 128, 128)  # Gray obstacles
 
# ============= GAME SYMBOLS =============
EMPTY, TREASURE, AGENT1, AGENT2, OBSTACLE = '.', 'T', 'A', 'B', 'X' 
 
# ============= PYGAME INITIALIZATION =============
pygame.init() 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Treasure Hunt - Manual + BFS Auto-Move") 
clock = pygame.time.Clock() 
 
def manhattan_dist(a, b):
    """Calculate Manhattan distance (used for treasure placement)
    Distance = |x1-x2| + |y1-y2|"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# ============= BUTTON CLASS =============
class Button:
    """Interactive button for 'Play Again' on win screen"""
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)  # Button area
        self.text = text
        self.color = (100, 150, 255)                  # Normal color
        self.hover_color = (50, 100, 200)             # Hover color
        self.is_hovered = False
        
    def draw(self, screen, font):
        """Draw button with hover effect"""
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 3)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def is_clicked(self, pos):
        """Check if button clicked"""
        return self.rect.collidepoint(pos)
    
    def update_hover(self, pos):
        """Update hover state"""
        self.is_hovered = self.rect.collidepoint(pos) 
 
# ============= MAIN GAME CLASS =============
class Game: 
    def __init__(self):
        """Initialize new game"""
        # Create 10x10 grid filled with EMPTY cells
        self.grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)] 
        # Agent1 at top-left (0,0), Agent2 at bottom-right (9,9)
        self.agent1 = (0, 0) 
        self.agent2 = (GRID_SIZE - 1, GRID_SIZE - 1) 
        self.place_treasure_far() 
        self.grid[self.agent1[0]][self.agent1[1]] = AGENT1 
        self.grid[self.agent2[0]][self.agent2[1]] = AGENT2 
        # Game state variables
        self.running = True
        self.moves_agent1 = 0  # Track moves for scoring
        self.moves_agent2 = 0
        self.start_time = time.time()  # Record start time
        self.font = pygame.font.Font(None, FONT_SIZE) 
    def place_treasure_far(self):
        """Place treasure randomly, 6+ cells from both agents (challenging)"""
        while True:
            pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            d1 = manhattan_dist(pos, self.agent1)  # Distance to Agent 1
            d2 = manhattan_dist(pos, self.agent2)  # Distance to Agent 2
            if d1 >= MIN_TREASURE_DIST and d2 >= MIN_TREASURE_DIST:
                self.treasure = pos
                self.grid[pos[0]][pos[1]] = TREASURE
                break 
 
    def can_move(self, pos, dx, dy):
        """Check if move is valid (in bounds and not blocked)"""
        nx, ny = pos[0] + dx, pos[1] + dy
        # Check bounds: 0 to GRID_SIZE-1
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            # Check cell not occupied by obstacle or other agent
            if self.grid[nx][ny] not in [OBSTACLE, AGENT1, AGENT2]:
                return True
        return False 
 
    def move_agent(self, agent_pos, dx, dy, symbol):
        """Move agent if possible and increment move counter"""
        if self.can_move(agent_pos, dx, dy):
            nx, ny = agent_pos[0] + dx, agent_pos[1] + dy
            self.grid[agent_pos[0]][agent_pos[1]] = EMPTY  # Clear old position
            agent_pos = (nx, ny)  # Update position
            self.grid[nx][ny] = symbol  # Mark new position
            # Increment move counter for scoring
            if symbol == AGENT1:
                self.moves_agent1 += 1
            else:
                self.moves_agent2 += 1
        return agent_pos 
 
    def place_obstacle(self, agent_pos):
        """Place obstacle next to agent in any empty direction"""
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
        for dx, dy in directions:
            nx, ny = agent_pos[0] + dx, agent_pos[1] + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                # Only place if empty and not treasure
                if self.grid[nx][ny] == EMPTY and (nx, ny) != self.treasure:
                    self.grid[nx][ny] = OBSTACLE
                    break 
 
    def bfs(self, start, goal, agent_symbol):
        """BFS (Breadth-First Search) - AI PATHFINDING ALGORITHM
        Finds shortest path to treasure using queue-based exploration
        Used for auto-move (press E or N)
        Returns: list of positions from start to goal, or None if no path"""
        queue = deque([start])      # Queue of positions to explore
        visited = {start: None}     # Track visited positions and their parents
 
        while queue:
            current = queue.popleft()  # Get next position
            if current == goal:  # Found treasure!
                # Reconstruct path backwards from goal to start
                path = []
                while current is not None:
                    path.append(current)
                    current = visited[current]
                path.reverse()  # Reverse to go from start to goal
                return path
 
            # Explore all 4 neighbors: up, down, left, right
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = current[0] + dx, current[1] + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                    if (nx, ny) not in visited:
                        cell = self.grid[nx][ny]
                        # Can move on empty cells and treasure
                        if cell in [EMPTY, TREASURE] or (nx, ny) == goal:
                            # Avoid opponent but allow moving into treasure
                            if agent_symbol == AGENT1 and cell != AGENT2:
                                visited[(nx, ny)] = current
                                queue.append((nx, ny))
                            elif agent_symbol == AGENT2 and cell != AGENT1:
                                visited[(nx, ny)] = current
                                queue.append((nx, ny))
        return None  # No path found 
 
    def auto_move_agent(self, agent_pos, symbol):
        """Auto-move: take one step along BFS path to treasure
        Triggered by E (Agent1) or N (Agent2)"""
        path = self.bfs(agent_pos, self.treasure, symbol)  # Get path to treasure
        if path and len(path) > 1:  # If path exists
            next_step = path[1]  # Get next position
            dx = next_step[0] - agent_pos[0]  # Calculate direction
            dy = next_step[1] - agent_pos[1]
            return self.move_agent(agent_pos, dx, dy, symbol)
        return agent_pos 
 
    def draw_grid(self):
        """Draw game grid with agents, treasure, and obstacles"""
        screen.fill(WHITE)  # Clear screen
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                cell = self.grid[row][col]
                # Draw colored rectangles based on cell type
                if cell == TREASURE:
                    pygame.draw.rect(screen, TREASURE_COLOR, rect)  # Gold
                elif cell == AGENT1:
                    pygame.draw.rect(screen, AGENT1_COLOR, rect)    # Blue
                elif cell == AGENT2:
                    pygame.draw.rect(screen, AGENT2_COLOR, rect)    # Red
                elif cell == OBSTACLE:
                    pygame.draw.rect(screen, OBSTACLE_COLOR, rect)  # Gray
                pygame.draw.rect(screen, BLACK, rect, 1)  # Grid borders

    def display_win_message(self, title, subtitle):
        """Display win screen with stats and PLAY AGAIN button"""
        elapsed_time = time.time() - self.start_time
        total_moves = self.moves_agent1 + self.moves_agent2
        # SCORE = 1000 - (moves × 10) - (time in seconds)
        score = max(0, 1000 - (total_moves * 10) - int(elapsed_time))
        
        # Print to console
        print(f"\n{'='*50}")
        print(f"  {title}")
        print(f"  {subtitle}")
        print(f"  Time: {elapsed_time:.1f} seconds")
        print(f"  Agent 1 Moves: {self.moves_agent1}")
        print(f"  Agent 2 Moves: {self.moves_agent2}")
        print(f"  SCORE: {score}")
        print(f"{'='*50}\n")
        
        # Create PLAY AGAIN button
        button = Button(WIDTH//2 - BUTTON_WIDTH//2, 380, BUTTON_WIDTH, BUTTON_HEIGHT, "PLAY AGAIN")
        
        # Display win screen until user action
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False  # User quit
                elif event.type == pygame.MOUSEMOTION:
                    button.update_hover(event.pos)  # Track hover
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button.is_clicked(event.pos):
                        return True  # User wants to play again
            
            # Draw win screen
            screen.fill(WHITE)
            title_text = self.font.render(title, True, (0, 128, 0))
            subtitle_text = self.font.render(subtitle, True, BLACK)
            time_text = self.font.render(f"Time: {elapsed_time:.1f}s", True, BLACK)
            moves1_text = self.font.render(f"Agent 1: {self.moves_agent1} moves", True, AGENT1_COLOR)
            moves2_text = self.font.render(f"Agent 2: {self.moves_agent2} moves", True, AGENT2_COLOR)
            score_text = pygame.font.Font(None, 40).render(f"SCORE: {score}", True, (255, 165, 0))
            
            # Display all text centered
            screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 50))
            screen.blit(subtitle_text, (WIDTH//2 - subtitle_text.get_width()//2, 100))
            screen.blit(time_text, (WIDTH//2 - time_text.get_width()//2, 150))
            screen.blit(moves1_text, (WIDTH//2 - moves1_text.get_width()//2, 210))
            screen.blit(moves2_text, (WIDTH//2 - moves2_text.get_width()//2, 260))
            screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 320))
            button.draw(screen, self.font)
            
            pygame.display.flip()
            clock.tick(30) 
 
    def play(self):
        """Main game loop - handle input, update state, render display"""
        while self.running:
            clock.tick(FPS)  # Maintain 10 FPS
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    # ===== AGENT 1 CONTROLS (Blue) =====
                    # W, A, S, D = Up, Left, Down, Right
                    if event.key == pygame.K_w:  # Up
                        self.agent1 = self.move_agent(self.agent1, -1, 0, AGENT1)
                    elif event.key == pygame.K_s:  # Down
                        self.agent1 = self.move_agent(self.agent1, 1, 0, AGENT1)
                    elif event.key == pygame.K_a:  # Left
                        self.agent1 = self.move_agent(self.agent1, 0, -1, AGENT1)
                    elif event.key == pygame.K_d:  # Right
                        self.agent1 = self.move_agent(self.agent1, 0, 1, AGENT1)
                    elif event.key == pygame.K_q:  # Place obstacle
                        self.place_obstacle(self.agent1)
                    elif event.key == pygame.K_e:  # Auto-move (BFS)
                        self.agent1 = self.auto_move_agent(self.agent1, AGENT1)
                    
                    # ===== AGENT 2 CONTROLS (Red) =====
                    # Arrow keys = Up, Down, Left, Right
                    elif event.key == pygame.K_UP:  # Up
                        self.agent2 = self.move_agent(self.agent2, -1, 0, AGENT2)
                    elif event.key == pygame.K_DOWN:  # Down
                        self.agent2 = self.move_agent(self.agent2, 1, 0, AGENT2)
                    elif event.key == pygame.K_LEFT:  # Left
                        self.agent2 = self.move_agent(self.agent2, 0, -1, AGENT2)
                    elif event.key == pygame.K_RIGHT:  # Right
                        self.agent2 = self.move_agent(self.agent2, 0, 1, AGENT2)
                    elif event.key == pygame.K_m:  # Place obstacle
                        self.place_obstacle(self.agent2)
                    elif event.key == pygame.K_n:  # Auto-move (BFS)
                        self.agent2 = self.auto_move_agent(self.agent2, AGENT2) 
 
            # ===== CHECK WIN CONDITIONS =====
            if self.agent1 == self.treasure and self.agent2 == self.treasure:
                # Both reach treasure together
                play_again = self.display_win_message("BOTH REACHED TREASURE!", "Cooperation Victory!")
                if not play_again:
                    self.running = False
                else:
                    return True  # Restart game
            elif self.agent1 == self.treasure:
                # Agent 1 wins
                play_again = self.display_win_message("AGENT 1 WINS!", f"Moves: {self.moves_agent1}")
                if not play_again:
                    self.running = False
                else:
                    return True
            elif self.agent2 == self.treasure:
                # Agent 2 wins
                play_again = self.display_win_message("AGENT 2 WINS!", f"Moves: {self.moves_agent2}")
                if not play_again:
                    self.running = False
                else:
                    return True
 
            self.draw_grid()  # Render game
            pygame.display.flip()  # Update display
 
        return False 
 
# ============= MAIN PROGRAM =============
if __name__ == "__main__":
    """Entry point - runs when script is executed"""
    playing = True
    while playing:
        game = Game()        # Create new game
        restart = game.play()  # Run game (returns True if "PLAY AGAIN" clicked)
        if not restart:      # If user quit
            playing = False
    pygame.quit()  # Clean up Pygame
