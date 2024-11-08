
# Autonomous Robot Navigation System

### Project Description
This project is a 2D autonomous robot navigation system designed to navigate through a grid-based environment using the A* pathfinding algorithm. The system calculates the optimal route from a start to a destination point and adapts dynamically to avoid obstacles in real time. Built with Python and visualized using Pygame, the project simulates autonomous navigation strategies and obstacle handling, with potential applications in robotics and autonomous vehicle systems.

### Features
- **A* Pathfinding**: Finds the shortest path from start to destination efficiently.
- **Dynamic Obstacle Avoidance**: Recalculates the path in real time as obstacles change.
- **Interactive Visualization**: Visualizes the robot's movement and pathfinding in a 2D grid.
  
### Technologies Used
- **Language**: Python
- **Libraries**: Pygame (for visualization)

### Getting Started

#### Prerequisites
- **Python 3.x**
- **Pygame** (install via pip):
  ```bash
  pip install pygame
  ```

#### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/SELVA-G-2003/robot-navigation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd robot-navigation
   ```
3. Run the main script to start the simulation:
   ```bash
   python main.py
   ```

### Usage
- Upon running, the simulation will display a grid where the robot starts from the designated **start** position and navigates to the **destination** while avoiding obstacles.
- Obstacles are randomly generated and may vary each time the simulation runs.

### Future Enhancements
- Additional pathfinding algorithms (e.g., Dijkstra’s, Greedy Best-First).
- Enhanced visualization with 3D effects or shadowing for more realistic depth.
- More sophisticated obstacle layouts and robot movement patterns.



