"""
Depth-First Search (DFS) for path in a grid (not guaranteed shortest).
"""

def dfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    stack = [start]
    visited = set([start])
    parent = {start: None}

    while stack:
        r, c = stack.pop()
        if (r, c) == goal:
            break

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                stack.append((nr, nc))

    # Reconstruct path
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent.get(node)
    return path[::-1]
