"""
Breadth-First Search (BFS) for shortest path in an unweighted grid.
"""

from collections import deque

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        r, c = queue.popleft()
        if (r, c) == goal:
            break

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc))

    # Reconstruct path
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent.get(node)
    return path[::-1]
