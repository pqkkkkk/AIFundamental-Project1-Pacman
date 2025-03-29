import time
import psutil
from collections import deque

def bfs_search(map, start, goal):
    start_time = time.time()
    process = psutil.Process()
    memory_before = process.memory_info().rss

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    came_from = {start: None}
    expanded_nodes = 0

    while queue:
        current = queue.popleft()
        expanded_nodes += 1

        if current == goal:
            memory_after = process.memory_info().rss
            search_time = time.time() - start_time
            memory_usage = (memory_after - memory_before) / (1024 * 1024)  

            print(f"Thời gian tìm kiếm: {search_time:.6f} giây")
            print(f"Bộ nhớ sử dụng: {memory_usage:.6f} MB")
            print(f"Số nút đã mở rộng: {expanded_nodes}")

            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(map) and 0 <= neighbor[1] < len(map[0]) and map[neighbor[0]][neighbor[1]] != 1:
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    queue.append(neighbor)

    memory_after = process.memory_info().rss
    search_time = time.time() - start_time
    memory_usage = (memory_after - memory_before) / (1024 * 1024)

    print(f"Thời gian tìm kiếm: {search_time:.6f} giây")
    print(f"Bộ nhớ sử dụng: {memory_usage:.6f} MB")
    print(f"Số nút đã mở rộng: {expanded_nodes}")

    return []


def dfs_search(map, start, goal):
    start_time = time.time()
    process = psutil.Process()
    memory_before = process.memory_info().rss

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [start]
    came_from = {start: None}
    expanded_nodes = 0

    while stack:
        current = stack.pop()
        expanded_nodes += 1

        if current == goal:
            memory_after = process.memory_info().rss
            search_time = time.time() - start_time
            memory_usage = (memory_after - memory_before) / (1024 * 1024)

            print(f"Thời gian tìm kiếm: {search_time:.6f} giây")
            print(f"Bộ nhớ sử dụng: {memory_usage:.6f} MB")
            print(f"Số nút đã mở rộng: {expanded_nodes}")

            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(map) and 0 <= neighbor[1] < len(map[0]) and map[neighbor[0]][neighbor[1]] != 1:
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    stack.append(neighbor)

    memory_after = process.memory_info().rss
    search_time = time.time() - start_time
    memory_usage = (memory_after - memory_before) / (1024 * 1024)

    print(f"Thời gian tìm kiếm: {search_time:.6f} giây")
    print(f"Bộ nhớ sử dụng: {memory_usage:.6f} MB")
    print(f"Số nút đã mở rộng: {expanded_nodes}")

    return []
