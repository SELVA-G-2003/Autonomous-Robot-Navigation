import pygame  # A Python library for creating 2D games and simulations.
import time  # Provides functions to control the simulation speed by adding delays between actions.
import random  # Allows random placement of obstacles in the warehouse
from queue import PriorityQueue # An efficient data structure used in A* pathfinding to prioritize nodes based on their estimated cost

# Initialize pygame and set up parameters
pygame.init()
width, height = 10, 10  # Setting the grid dimensions of the warehouse (10x10 cells)
cell_size = 50  # Specifying each cell’s size in pixels
screen = pygame.display.set_mode((width * cell_size, height * cell_size))
pygame.display.set_caption("Autonomous Robot Navigation By G SELVA")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

# Robot and path parameters
start = (0, 0)
destination = (7, 9)
robot_speed = 0.1  # seconds for movement simulation
robot_pause = 2  # seconds for robot pause after every step


# Generating random obstacles that do not overlap with start or destination
def generate_obstacles(num_obstacles, start, destination):
    obstacles = set()  # Storing obstacles to avoid duplicate placements
    while len(obstacles) < num_obstacles:
        obstacle = (random.randint(0, width - 1), random.randint(0, height - 1))
        if (
            obstacle != start and obstacle != destination # Ensuring the obstacles doesn’t overlap the start or destination positions
        ):  
            obstacles.add(obstacle)
    return list(obstacles)  # Converting the set to a list for use in the simulation


# Generating a random set of obstacles
obstacles = generate_obstacles(num_obstacles=8, start=start, destination=destination)


# A* Pathfinding algorithm(The A*(A-star) algorithm is a widely-used pathfinding algorithm in computer science, especially for games and navigation systems)
def a_star(start, destination):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, destination)}

    while not open_set.empty():
        current = open_set.get()[1]

        if current == destination:
            print("Path found! Starting the robot's journey...")
            return path_reconstruction(came_from, current)

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, destination)
                if not any(neighbor == item[1] for item in open_set.queue):
                    open_set.put((f_score[neighbor], neighbor))

    return []


# Calculating the initial f_score for the start node, using the Manhattan distance(Manhattan Distance=∣X2−X1∣+∣Y2−Y1∣)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Returns valid neighbors of position, considering grid boundaries and obstacles
def get_neighbors(position):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbor = (position[0] + dx, position[1] + dy)
        if (
            0 <= neighbor[0] < width
            and 0 <= neighbor[1] < height
            and neighbor not in obstacles
        ):
            neighbors.append(neighbor)
    return neighbors


# Reconstructing the path by tracing backward from destination to start using came_from
def path_reconstruction(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]  # Reverses the list for a start-to-goal sequence


# Function to draw the warehouse, path, and robot
def generate_warehouse(path, position):
    screen.fill(WHITE)

    # Draw obstacles
    for obs in obstacles:
        pygame.draw.rect(
            screen, RED, (obs[0] * cell_size, obs[1] * cell_size, cell_size, cell_size)
        )

    # Draw start and destination
    pygame.draw.circle(
        screen,
        GREEN,
        (start[0] * cell_size + cell_size // 2, start[1] * cell_size + cell_size // 2),
        cell_size // 3,
    )
    pygame.draw.circle(
        screen,
        BLUE,
        (
            destination[0] * cell_size + cell_size // 2,
            destination[1] * cell_size + cell_size // 2,
        ),
        cell_size // 3,
    )

    # Draw path
    for node in path:
        pygame.draw.rect(
            screen,
            CYAN,
            (node[0] * cell_size, node[1] * cell_size, cell_size, cell_size),
            1,
        )

    # Draw robot
    pygame.draw.circle(
        screen,
        BLACK,
        (
            position[0] * cell_size + cell_size // 2,
            position[1] * cell_size + cell_size // 2,
        ),
        cell_size // 3,
    )

    # Display labels for start, destination, and robot
    font = pygame.font.Font(None, 24)
    screen.blit(
        font.render("Start", True, GREEN),
        (start[0] * cell_size + cell_size, start[1] * cell_size),
    )
    screen.blit(
        font.render("Destination", True, BLUE),
        (destination[0] * cell_size + cell_size, destination[1] * cell_size),
    )
    screen.blit(
        font.render("Robot", True, BLACK),
        (position[0] * cell_size, position[1] * cell_size - 20),
    )

    pygame.display.flip()  # Update display


# Controlling the robot’s movement along the path calculated by A*
def move_robot():
    path = a_star(start, destination)
    if not path:
        print("No valid path found to the destination.")
        return

    for position in path:
        for event in pygame.event.get():  # Allow quitting the simulation
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        generate_warehouse(path, position)
        time.sleep(robot_speed + robot_pause)  # Simulate pause with movement


# Run the simulation
move_robot()
# Quit when the simulation completes
pygame.quit()
