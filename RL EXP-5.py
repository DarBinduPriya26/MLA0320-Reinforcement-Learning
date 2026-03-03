# Grid size
size = 5
gamma = 0.9

# Pickup locations
pickup_points = [(4,4), (2,2)]

# Actions: Up, Down, Left, Right
actions = [(-1,0),(1,0),(0,-1),(0,1)]

# Initialize Value Function
V = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    V.append(row)

# Policy
policy = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    policy.append(row)


def next_state(x, y, action):
    dx, dy = actions[action]
    nx = x + dx
    ny = y + dy

    if 0 <= nx < size and 0 <= ny < size:
        return nx, ny
    return x, y


# -------- Value Iteration --------
for iteration in range(100):

    new_V = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        new_V.append(row)

    for i in range(size):
        for j in range(size):

            if (i,j) in pickup_points:
                new_V[i][j] = 0
                continue

            best_value = -999

            for a in range(4):
                nx, ny = next_state(i,j,a)

                if (nx,ny) in pickup_points:
                    reward = 100
                else:
                    reward = -1

                value = reward + gamma * V[nx][ny]

                if value > best_value:
                    best_value = value
                    policy[i][j] = a

            new_V[i][j] = best_value

    V = new_V


print("Optimal Value Function:")
for row in V:
    print(row)

print("\nOptimal Policy (0=Up,1=Down,2=Left,3=Right):")
for row in policy:
    print(row)
