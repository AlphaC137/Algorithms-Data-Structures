import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from bfs import bfs

def generate_grid(rows, cols, obstacle_prob=0.2):
    grid = [[0 if random.random() > obstacle_prob else 1 for _ in range(cols)] for _ in range(rows)]
    grid[0][0] = 0
    grid[rows-1][cols-1] = 0
    return grid

def visualize():
    rows, cols = 20, 20
    grid = generate_grid(rows, cols)
    start, goal = (0,0), (rows-1, cols-1)

    path = bfs(grid, start, goal)

    fig, ax = plt.subplots()
    ax.set_title("BFS Pathfinding")
    ax.imshow(grid, cmap="gray_r")

    path_x = [x for x,y in path]
    path_y = [y for x,y in path]
    ax.plot([p[1] for p in path], [p[0] for p in path], color="red")

    plt.show()

if __name__ == "__main__":
    visualize()
