import random
import math

# True click probabilities for ads
prob = [0.1, 0.15, 0.05, 0.2]

rounds = 1000


def get_click(ad):
    if random.random() < prob[ad]:
        return 1
    return 0


# -------- Epsilon Greedy --------
def epsilon_greedy(epsilon):
    counts = [0,0,0,0]
    values = [0,0,0,0]
    total_clicks = 0

    for t in range(rounds):

        if random.random() < epsilon:
            ad = random.randint(0,3)
        else:
            ad = values.index(max(values))

        reward = get_click(ad)
        counts[ad] += 1
        values[ad] += (reward - values[ad]) / counts[ad]
        total_clicks += reward

    return total_clicks


# -------- UCB --------
def ucb():
    counts = [0,0,0,0]
    values = [0,0,0,0]
    total_clicks = 0

    for t in range(rounds):

        if t < 4:
            ad = t
        else:
            ucb_values = []
            for i in range(4):
                bonus = math.sqrt((2 * math.log(t+1)) / counts[i])
                ucb_values.append(values[i] + bonus)

            ad = ucb_values.index(max(ucb_values))

        reward = get_click(ad)
        counts[ad] += 1
        values[ad] += (reward - values[ad]) / counts[ad]
        total_clicks += reward

    return total_clicks


# -------- Thompson Sampling --------
def thompson():
    success = [1,1,1,1]
    failure = [1,1,1,1]
    total_clicks = 0

    for t in range(rounds):

        samples = []
        for i in range(4):
            samples.append(random.betavariate(success[i], failure[i]))

        ad = samples.index(max(samples))

        reward = get_click(ad)

        if reward == 1:
            success[ad] += 1
        else:
            failure[ad] += 1

        total_clicks += reward

    return total_clicks


print("Epsilon Greedy Clicks:", epsilon_greedy(0.1))
print("UCB Clicks:", ucb())
print("Thompson Sampling Clicks:", thompson())
