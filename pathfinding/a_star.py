"""
A* Search Algorithm with Manhattan heuristic.
"""

import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    g = {start: 0}
    f = {start: heuristic(start, goal)}
    pq = [(f[start], start)]
    parent = {start: None}

    while pq:
        _, (r, c) = heapq.heappop(pq)
        if (r, c) == goal:
            break

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_g = g[(r, c)] + 1
                if (nr, nc) not in g or new_g < g[(nr, nc)]:
                    g[(nr, nc)] = new_g
                    f[(nr, nc)] = new_g + heuristic((nr, nc), goal)
                    parent[(nr, nc)] = (r, c)
                    heapq.heappush(pq, (f[(nr, nc)], (nr, nc)))

    # Reconstruct path
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent.get(node)
    return path[::-1]
