import random
import math

# Price options and true purchase probabilities
prices = [100, 120, 150, 180, 200]
true_probs = [0.30, 0.25, 0.20, 0.15, 0.10]
steps = 1000

# Simulate reward
def get_reward(arm):
    if random.random() < true_probs[arm]:
        return prices[arm]
    return 0

# -------- Epsilon Greedy --------
def epsilon_greedy(epsilon=0.1):
    counts = [0]*5
    values = [0]*5
    total_reward = 0

    for t in range(steps):
        if random.random() < epsilon:
            arm = random.randint(0, 4)
        else:
            arm = values.index(max(values))

        reward = get_reward(arm)
        counts[arm] += 1
        values[arm] += (reward - values[arm]) / counts[arm]
        total_reward += reward

    return total_reward

# -------- UCB --------
def ucb():
    counts = [0]*5
    values = [0]*5
    total_reward = 0

    for t in range(steps):
        if 0 in counts:
            arm = counts.index(0)
        else:
            ucb_values = [
                values[i] + math.sqrt((2 * math.log(t)) / counts[i])
                for i in range(5)
            ]
            arm = ucb_values.index(max(ucb_values))

        reward = get_reward(arm)
        counts[arm] += 1
        values[arm] += (reward - values[arm]) / counts[arm]
        total_reward += reward

    return total_reward
# -------- Thompson Sampling --------
def thompson():
    successes = [1]*5
    failures = [1]*5
    total_reward = 0

    for t in range(steps):
        samples = [random.betavariate(successes[i], failures[i]) for i in range(5)]
        arm = samples.index(max(samples))

        reward = get_reward(arm)
        if reward > 0:
            successes[arm] += 1
        else:
            failures[arm] += 1

        total_reward += reward

    return total_reward


print("Epsilon-Greedy Revenue:", epsilon_greedy())
print("UCB Revenue:", ucb())
print("Thompson Sampling Revenue:", thompson())
