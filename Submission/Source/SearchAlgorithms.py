import heapq
    # start, goal là toạ độ (x,y) trong map
    # map là 1 ma trận 2 chiều (m,n)
def UCS_Algorithm(map, start, goal):
    frontier = []
    explored = []
    path = []
    moves = [(-1,0), (0, -1), (1, 0), (0, 1)]
    # ban đầu, khởi tạo trạng thái hiẹn tại = start
    currentState = start     
    heapq.heappush(frontier,(0, start, path))
        
    while frontier:
        pathCost, currentState, path = heapq.heappop(frontier)
        path += [currentState]    
        explored.append(currentState)

        if(currentState == goal):
            return pathCost, path

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

    return None, None 
     
        
# map = [
#     [0, 0, 1, 1],
#     [0, 0, 1, 0],
#     [1, 0, 0, 0],
#     [1, 0, 1, 0],
#     [1, 0, 0, 0]
# ]

# start = (0, 0)
# goal = (4, 3)

# cost, path = UCS_Algorithm(map, start, goal)
# print('chi phi:', cost)
# print('duong di:', path)
