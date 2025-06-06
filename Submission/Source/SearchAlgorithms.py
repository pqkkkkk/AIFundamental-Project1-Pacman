import heapq
import time
import psutil
from collections import deque
timeSpend = 0
memoryUsage = 0
expandedNode = 0

def heuristic_func(cur, goal):
    " Heuristic: Dùng công thức Manhattan tích khoảng cách từ vị trí hiện tại đến PacMan "
    return abs(cur[0] - goal[0]) + abs(cur[1] - goal[1])

def is_valid_position(cur, map):
    " Kiểm tra tính hợp lệ của vị trí hiện tại (không vượt ra ngoài, không dính tường)"
    x, y = cur
    return 0 <= x < len(map) and 0 <= y < len(map[0]) and map[x][y] == 0

def reconstruct_path(came_from, current, start):
    "Xây dựng lại đường đi từ Goal đến Start"
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def a_star_search(map, start, goal):
     # Thời gian bắt đầu
    global timeSpend, memoryUsage, expandedNode
    start_time = time.time()
    
    # Bộ nhớ ban đầu
    process = psutil.Process()
    memory_before = process.memory_info().rss 
    "Dùng thuật toán A* để tìm đường đi ngắn nhất"
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Di chuyển: lên, xuống, trái, phải
    frontier = []  # Hàng đợi ưu tiên (priority queue)
    heapq.heappush(frontier, (0, start))  # (f_score, vị trí)

    came_from = {}  # Để dựng lại đường đi
    g_score = {start: 0}  # g(n): chi phí từ start đến mỗi ô
    f_score = {start: heuristic_func(start, goal)}  # f(n) = g(n) + h(n)

    expandedNode = 0  # Biến đếm số nút đã mở rộng

    while frontier:
        _, current = heapq.heappop(frontier)  # Lấy ô có f-score thấp nhất
        expandedNode += 1  # Mỗi lần lấy một ô ra, ta coi như đã mở rộng nó

        if current == goal:
            memory_after = process.memory_info().rss  
            timeSpend = time.time() - start_time
            memoryUsage = (memory_after - memory_before) / (1024 * 1024)  # Đổi sang MB

            return reconstruct_path(came_from, current,start)  # Trả về đường đi tối ưu

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if is_valid_position(neighbor, map): # tentative_g_score là giá trị tạm thời của g_score = start => neighbor
                tentative_g_score = g_score[current] + 1  # Mỗi bước đi có chi phí 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:# Nếu chi phí tạm thời nhỏ hơn chi phí đã biết hoặc chưa duyệt qua neighbor
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score # cập nhật lại đường đi
                    f_score[neighbor] = tentative_g_score + heuristic_func(neighbor, goal)
                    heapq.heappush(frontier, (f_score[neighbor], neighbor))

    memory_after = process.memory_info().rss  
    timeSpend = time.time() - start_time
    memoryUsage = (memory_after - memory_before) / (1024 * 1024)  # Đổi sang MB


    return []  # Không tìm thấy đường đi
  
def bfs_search(map, start, goal):
    global timeSpend, memoryUsage, expandedNode
    start_time = time.time()
    process = psutil.Process()
    memory_before = process.memory_info().rss

    directions = [(-1,0), (0,-1), (1, 0), (0, 1)]
    queue = deque([start])
    came_from = {start: None}
    expandedNode = 0

    while queue:
        current = queue.popleft()
        expandedNode += 1

        if current == goal:
            memory_after = process.memory_info().rss
            timeSpend = time.time() - start_time
            memoryUsage = (memory_after - memory_before) / (1024 * 1024)  

            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(map) and 0 <= neighbor[1] < len(map[0]) and map[neighbor[0]][neighbor[1]] == 0:
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    queue.append(neighbor)

    memory_after = process.memory_info().rss
    timeSpend = time.time() - start_time
    memoryUsage = (memory_after - memory_before) / (1024 * 1024)

    return []

def dfs_search(map, start, goal):
    global timeSpend, memoryUsage, expandedNode
    start_time = time.time()
    process = psutil.Process()
    memory_before = process.memory_info().rss

    directions = [(-1,0), (0, -1), (1, 0), (0, 1)]
    stack = [start]
    came_from = {start: None}
    expandednode = 0

    while stack:
        current = stack.pop()
        expandedNode += 1

        if current == goal:
            memory_after = process.memory_info().rss
            timeSpend = time.time() - start_time
            memoryUsage = (memory_after - memory_before) / (1024 * 1024)

            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(map) and 0 <= neighbor[1] < len(map[0]) and map[neighbor[0]][neighbor[1]] == 0:
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    stack.append(neighbor)

    memory_after = process.memory_info().rss
    timeSpend = time.time() - start_time
    memoryUsage = (memory_after - memory_before) / (1024 * 1024)

    return []

    # start, goal là toạ độ (x,y) trong map
    # map là 1 ma trận 2 chiều (m,n)
def ucs_search(map, start, goal):
    global timeSpend, memoryUsage, expandedNode
    start_time = time.time()
    # Bộ nhớ ban đầu
    process = psutil.Process()
    memory_before = process.memory_info().rss 
    expandedNode = 0
    frontier = []
    explored = []
    path = []
    moves = [(-1,0), (0, -1), (1, 0), (0, 1)]
    # ban đầu, khởi tạo trạng thái hiẹn tại = start
    currentState = start     
    heapq.heappush(frontier,(0, start, path))
    
    while frontier:
        pathCost, currentState, path = heapq.heappop(frontier)
        expandedNode += 1

        path += [currentState]
        explored.append(currentState)

        if(currentState == goal):
            memory_after = process.memory_info().rss
            timeSpend = time.time() - start_time
            memoryUsage = (memory_after - memory_before) / (1024 * 1024)

            return path

        # Kiểm tra 4 hướng (x-1, y), (x, y-1), (x+1, y), (x, y + 1), 
        for dx, dy in moves:
            nx , ny = currentState[0] + dx, currentState[1] + dy
            estimatedCost = pathCost + 1
            if ( 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] == 0):
                # Kiểm tra nếu vị trí hiện tại chưa được thăm và chưa nằm trong frontier
                found = any(item[1] == (nx, ny) for item in frontier)
                if((nx, ny) not in explored and not found):
                    new_path = path[:]
                    heapq.heappush(frontier,(estimatedCost, (nx, ny), new_path))
                elif(found and estimatedCost < pathCost):
                    for i, item in enumerate(frontier):
                        if item[1] == (nx, ny):
                            frontier[i] = (estimatedCost, item[1], new_path)
                    break

    return None
