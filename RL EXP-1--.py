# 5x5 Grid
grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],   # dirt = 1
    [0, 0, -1, 0, 0],  # obstacle = -1
    [0, -1, 0, 1, 0],
    [0, 1, 0, 0, 0]
]

x, y = 0, 0   # start position
total_reward = 0

print("Robot Path:")

# Simple policy: move right till end, then move down
while x < 5 and y < 5:
    
    print("Position:", x, y)
    
    # Collect reward
    if grid[x][y] == 1:
        total_reward += 1
        grid[x][y] = 0   # clean dirt
    
    if grid[x][y] == -1:
        total_reward -= 1
    
    # Move Right if possible else Down
    if y < 4:
        y += 1
    else:
        x += 1
        y = 0
    
    if x == 5:
        break

print("Total Reward:", total_reward)
