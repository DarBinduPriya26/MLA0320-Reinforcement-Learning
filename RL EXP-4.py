# Grid size
size = 5
gamma = 0.9

# Delivery points (multiple goals)
goals = [(4,4), (2,3)]

# Actions: Up, Down, Left, Right
actions = [(-1,0),(1,0),(0,-1),(0,1)]

# Initialize value function and policy
V = []
policy = []

for i in range(size):
    row_v = []
    row_p = []
    for j in range(size):
        row_v.append(0)
        row_p.append(0)
    V.append(row_v)
    policy.append(row_p)


def next_state(x, y, action):
    dx, dy = actions[action]
    nx = x + dx
    ny = y + dy

    if 0 <= nx < size and 0 <= ny < size:
        return nx, ny
    return x, y


stable = False

while not stable:

    # -------- Policy Evaluation --------
    for k in range(20):
        for i in range(size):
            for j in range(size):

                if (i,j) in goals:
                    continue

                action = policy[i][j]
                nx, ny = next_state(i, j, action)

                if (nx,ny) in goals:
                    reward = 100
                else:
                    reward = -1

                V[i][j] = reward + gamma * V[nx][ny]

    # -------- Policy Improvement --------
    stable = True

    for i in range(size):
        for j in range(size):

            if (i,j) in goals:
                continue

            old_action = policy[i][j]
            best_value = -999
            best_action = 0

            for a in range(4):
                nx, ny = next_state(i, j, a)

                if (nx,ny) in goals:
                    reward = 100
                else:
                    reward = -1

                value = reward + gamma * V[nx][ny]

                if value > best_value:
                    best_value = value
                    best_action = a

            policy[i][j] = best_action

            if old_action != best_action:
                stable = False


print("Optimal Value Function:")
for row in V:
    print(row)

print("\nOptimal Policy (0=Up,1=Down,2=Left,3=Right):")
for row in policy:
    print(row)
