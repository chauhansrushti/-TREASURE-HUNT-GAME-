import pygame 
import random 
import time 
from collections import deque 
 
# Constants 
GRID_SIZE = 10 
CELL_SIZE = 60 
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE 
FPS = 10 
MIN_TREASURE_DIST = 6  # minimum Manhattan distance from agents 
 
# Colors 
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
TREASURE_COLOR = (255, 215, 0) 
AGENT1_COLOR = (0, 128, 255) 
AGENT2_COLOR = (255, 0, 0)  
OBSTACLE_COLOR = (128, 128, 128) 
 
# Game symbols 
EMPTY, TREASURE, AGENT1, AGENT2, OBSTACLE = '.', 'T', 'A', 'B', 'X' 
 
# Initialize pygame 
pygame.init() 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Treasure Hunt - Manual + BFS Auto-Move") 
clock = pygame.time.Clock() 
 
def manhattan_dist(a, b): 
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 
 
class Game: 
    def __init__(self): 
        self.grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)] 
        self.agent1 = (0, 0) 
        self.agent2 = (GRID_SIZE - 1, GRID_SIZE - 1) 
        self.place_treasure_far() 
        self.grid[self.agent1[0]][self.agent1[1]] = AGENT1 
        self.grid[self.agent2[0]][self.agent2[1]] = AGENT2 
        self.running = True 
    def place_treasure_far(self): 
 
        while True: 
            pos = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)) 
            d1 = manhattan_dist(pos, self.agent1) 
            d2 = manhattan_dist(pos, self.agent2) 
            if d1 >= MIN_TREASURE_DIST and d2 >= MIN_TREASURE_DIST: 
                self.treasure = pos 
                self.grid[pos[0]][pos[1]] = TREASURE 
                break 
 
    def can_move(self, pos, dx, dy): 
        nx, ny = pos[0] + dx, pos[1] + dy 
        if 0 <= nx< GRID_SIZE and 0 <= ny< GRID_SIZE: 
            if self.grid[nx][ny] not in [OBSTACLE, AGENT1, AGENT2]: 
                return True 
        return False 
 
    def move_agent(self, agent_pos, dx, dy, symbol): 
        if self.can_move(agent_pos, dx, dy): 
            nx, ny = agent_pos[0] + dx, agent_pos[1] + dy 
            self.grid[agent_pos[0]][agent_pos[1]] = EMPTY 
            agent_pos = (nx, ny) 
            self.grid[nx][ny] = symbol 
        return agent_pos 
 
    def place_obstacle(self, agent_pos): 
        directions = [(-1,0), (1,0), (0,-1), (0,1)] 
        for dx, dy in directions:  
            nx, ny = agent_pos[0] + dx, agent_pos[1] + dy 
            if 0 <= nx< GRID_SIZE and 0 <= ny< GRID_SIZE: 
                if self.grid[nx][ny] == EMPTY and (nx, ny) != self.treasure: 
                    self.grid[nx][ny] = OBSTACLE 
                    break 
 
    def bfs(self, start, goal, agent_symbol): 
        queue = deque([start]) 
        visited = {start: None} 
 
        while queue: 
            current = queue.popleft() 
            if current == goal: 
                # Reconstruct path from goal to start 
                path = [] 
                while current is not None: 
                    path.append(current) 
                    current = visited[current] 
                path.reverse() 
                return path  # path includes start and goal 
 
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]: 
                nx, ny = current[0] + dx, current[1] + dy 
                if 0 <= nx< GRID_SIZE and 0 <= ny< GRID_SIZE: 
                   
if (nx, ny) not in visited:  
                        cell = self.grid[nx][ny] 
                        # Can step on EMPTY or TREASURE but NOT on obstacles or other agent 
                        if cell in [EMPTY, TREASURE] or (nx, ny) == goal: 
                            # Avoid blocking own position or opponent's position 
                            # But allow moving into treasure cell 
                            if agent_symbol == AGENT1 and cell != AGENT2: 
                                visited[(nx, ny)] = current 
                                queue.append((nx, ny)) 
                            elifagent_symbol == AGENT2 and cell != AGENT1: 
                                visited[(nx, ny)] = current 
                                queue.append((nx, ny)) 
        return None  # no path found 
 
    def auto_move_agent(self, agent_pos, symbol): 
        path = self.bfs(agent_pos, self.treasure, symbol) 
        if path and len(path) > 1: 
            next_step = path[1] 
            dx = next_step[0] - agent_pos[0] 
            dy = next_step[1] - agent_pos[1] 
            return self.move_agent(agent_pos, dx, dy, symbol) 
        return agent_pos 
 
    def draw_grid(self): 
        screen.fill(WHITE) 
       
  for row in range(GRID_SIZE):  
            for col in range(GRID_SIZE): 
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE) 
                cell = self.grid[row][col] 
                if cell == TREASURE: 
                    pygame.draw.rect(screen, TREASURE_COLOR, rect) 
                elif cell == AGENT1: 
                    pygame.draw.rect(screen, AGENT1_COLOR, rect) 
                elif cell == AGENT2: 
                    pygame.draw.rect(screen, AGENT2_COLOR, rect) 
                elif cell == OBSTACLE: 
                    pygame.draw.rect(screen, OBSTACLE_COLOR, rect) 
                pygame.draw.rect(screen, BLACK, rect, 1) 
 
    def play(self): 
        while self.running: 
            clock.tick(FPS) 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.running = False 
                elifevent.type == pygame.KEYDOWN: 
                    # Agent1 manual move WASD 
                    if event.key == pygame.K_w: 
                        self.agent1 = self.move_agent(self.agent1, -1, 0, AGENT1) 
                    elifevent.key == pygame.K_s: 
                      
   self.agent1 = self.move_agent(self.agent1, 1, 0, AGENT1)  
                    elifevent.key == pygame.K_a: 
                        self.agent1 = self.move_agent(self.agent1, 0, -1, AGENT1) 
                    elifevent.key == pygame.K_d: 
                        self.agent1 = self.move_agent(self.agent1, 0, 1, AGENT1) 
                    # Agent1 place obstacle Q 
                    elifevent.key == pygame.K_q: 
                        self.place_obstacle(self.agent1) 
                    # Agent1 auto move step E 
                    elifevent.key == pygame.K_e: 
                        self.agent1 = self.auto_move_agent(self.agent1, AGENT1) 
 
                    # Agent2 manual move Arrows 
                    elifevent.key == pygame.K_UP: 
                        self.agent2 = self.move_agent(self.agent2, -1, 0, AGENT2) 
                    elifevent.key == pygame.K_DOWN: 
                        self.agent2 = self.move_agent(self.agent2, 1, 0, AGENT2) 
                    elifevent.key == pygame.K_LEFT: 
                        self.agent2 = self.move_agent(self.agent2, 0, -1, AGENT2) 
                    elifevent.key == pygame.K_RIGHT: 
                        self.agent2 = self.move_agent(self.agent2, 0, 1, AGENT2) 
                    # Agent2 place obstacle M 
                    elifevent.key == pygame.K_m: 
                        self.place_obstacle(self.agent2) 
                    # Agent2 auto move step N 
                     
elifevent.key == pygame.K_n: 
                        self.agent2 = self.auto_move_agent(self.agent2, AGENT2) 
 
            # Win check 
            if self.agent1 == self.treasure and self.agent2 == self.treasure: 
                print("🤝 Both reached the treasure!") 
                self.running = False 
            elifself.agent1 == self.treasure: 
                print("🤝 Agent1 Wins!") 
                self.running = False 
            elifself.agent2 == self.treasure: 
                print("🤝 Agent2 Wins!") 
                self.running = False 
 
            self.draw_grid() 
            pygame.display.flip() 
 
        time.sleep(2) 
        pygame.quit() 
 
if __name__ == "__main__": 
    Game().play() 
 
 
 
 
OUTPUT:-
