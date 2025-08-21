"""
Dijkstra’s Algorithm for weighted grids/graphs.
"""

import heapq

def dijkstra(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    dist = {start: 0}
    pq = [(0, start)]
    parent = {start: None}

    while pq:
        d, (r, c) = heapq.heappop(pq)
        if (r, c) == goal:
            break
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cost = grid[nr][nc]  # weight of cell
                new_dist = d + cost
                if (nr, nc) not in dist or new_dist < dist[(nr, nc)]:
                    dist[(nr, nc)] = new_dist
                    parent[(nr, nc)] = (r, c)
                    heapq.heappush(pq, (new_dist, (nr, nc)))

    # Reconstruct path
    path = []
    node = goal
    while node:
        path.append(node)
        node = parent.get(node)
    return path[::-1]
