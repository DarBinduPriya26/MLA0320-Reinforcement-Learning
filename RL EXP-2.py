# 4x4 Warehouse Grid
grid = [
    [0, 0, 0, 0],
    [0, 2, 0, 0],   # item = +2
    [0, 0, -2, 0],  # obstacle = -2
    [0, 0, 0, 5]    # goal = +5
]

gamma = 0.9
V = [[0 for j in range(4)] for i in range(4)]

# Policy Evaluation (5 iterations only)
for k in range(5):
    newV = [[0 for j in range(4)] for i in range(4)]
    
    for i in range(4):
        for j in range(4):
            
            if grid[i][j] == -2:
                continue
            
            value = 0
            
            # 4 possible moves
            moves = [(-1,0),(1,0),(0,-1),(0,1)]
            
            for move in moves:
                ni = i + move[0]
                nj = j + move[1]
                
                if 0 <= ni < 4 and 0 <= nj < 4 and grid[ni][nj] != -2:
                    reward = grid[ni][nj]
                    value += 0.25 * (reward + gamma * V[ni][nj])
            
            newV[i][j] = value
    
    V = newV

print("Value Function:")
for row in V:
    print(row)
