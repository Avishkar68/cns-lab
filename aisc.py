# ============================================================
# EXPERIMENT 1: INTELLIGENT AGENTS IN A GRID ENVIRONMENT
# ============================================================

from collections import deque


# Grid representation
grid = [
    ['.', '.', '.', '.', '.'],
    ['.', 'X', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', 'X', '.', '.', 'C'],
    ['.', '.', '.', '.', '.']
]

# Movement: Right, Down, Left, Up
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# Check whether a position is valid
def valid(r, c):
    return 0 <= r < 5 and 0 <= c < 5 and grid[r][c] != 'X'


# Display the grid
def show(r, c):
    for i in range(5):
        for j in range(5):
            if i == r and j == c:
                print("R", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()
    print()


# 1. Simple Reflex Agent
def reflex(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if valid(nr, nc):
            return nr, nc

    return r, c


# 2. Model-Based Agent
def model(r, c, visited):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if valid(nr, nc) and not visited[nr][nc]:
            visited[nr][nc] = True
            return nr, nc

    return reflex(r, c)


# 3. Goal-Based Agent (BFS)
def bfs(sr, sc, gr, gc):
    q = deque()
    visited = [[False] * 5 for _ in range(5)]

    q.append((sr, sc))
    visited[sr][sc] = True

    while q:
        r, c = q.popleft()
        show(r, c)

        if r == gr and c == gc:
            print("Goal Reached!")
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if valid(nr, nc) and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))

    print("Goal Not Found!")


# 4. Utility-Based Agent
def utility(r, c):
    x = [3, 0, 4]
    y = [4, 4, 0]
    priority = [1, 3, 2]

    best = -999
    bx = -1
    by = -1

    for i in range(3):
        robot_x = x[i]
        robot_y = y[i]

        distance = abs(r - robot_x) + abs(c - robot_y)
        u = priority[i] * 20 - distance * 5

        print("Customer", i + 1, "Utility =", u)

        if u > best:
            best = u
            bx = x[i]
            by = y[i]

    print("Best Customer:", (bx, by))


# Main Program
def main():
    r, c = 2, 2

    print("1. Reflex Agent")
    for i in range(10):
        r, c = reflex(r, c)
        print("Position:", r, c)

    print("\n2. Model-Based Agent")
    r, c = 2, 2
    visited = [[False] * 5 for _ in range(5)]
    visited[r][c] = True

    for i in range(25):
        r, c = model(r, c, visited)

        if r == 3 and c == 4:
            break

    print("Position:", r, c)

    print("\n3. Goal-Based Agent (BFS)")
    bfs(2, 2, 3, 4)

    print("\n4. Utility-Based Agent")
    utility(2, 2)


if __name__ == "__main__":
    main()


# ============================================================
# EXPERIMENT 3: ACTIVATION FUNCTIONS AND ADDER IMPLEMENTATION
# ============================================================

import math


# Activation functions
def step(x):
    return 1 if x >= 0 else 0


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def tanh(x):
    return math.tanh(x)


def relu(x):
    return max(0, x)


def leaky_relu(x):
    return x if x > 0 else 0.01 * x


def softmax(a, b):
    x = math.exp(a)
    y = math.exp(b)

    return x / (x + y), y / (x + y)


# Neuron
def neuron(a, b, w1, w2, bias):
    return step(a * w1 + b * w2 + bias)


# Half Adder
def half_adder(a, b):
    OR = neuron(a, b, 1, 1, -0.5)
    AND = neuron(a, b, 1, 1, -1.5)

    SUM = neuron(OR, AND, 1, -1, -0.5)
    CARRY = AND

    return SUM, CARRY


# Full Adder
def full_adder(a, b, cin):
    s1, c1 = half_adder(a, b)
    s, c2 = half_adder(s1, cin)

    cout = step(c1 + c2 - 0.5)

    return s, cout


# Half Adder Truth Table
print("HALF ADDER")
print("A B | Sum Carry")

for a in range(2):
    for b in range(2):
        s, c = half_adder(a, b)
        print(a, b, "|", s, c)


# Full Adder Truth Table
print("\nFULL ADDER")
print("A B Cin | Sum Carry")

for a in range(2):
    for b in range(2):
        for cin in range(2):
            s, c = full_adder(a, b, cin)
            print(a, b, cin, "|", s, c)


# Activation functions on Half Adder outputs
print("\nACTIVATION FUNCTIONS")

for a in range(2):
    for b in range(2):
        s, c = half_adder(a, b)

        print("\nInputs:", a, b)
        print("Sigmoid:", sigmoid(s), sigmoid(c))
        print("Tanh:", tanh(s), tanh(c))
        print("ReLU:", relu(s), relu(c))
        print("Leaky ReLU:", leaky_relu(s), leaky_relu(c))
        print("Softmax:", softmax(s, c))


# ============================================================
# EXPERIMENT 4: SINGLE LAYER PERCEPTRON
# ============================================================

# Single Layer Perceptron
def step(x):
    return 1 if x >= 0 else 0


def train(X, T, lr=0.1, epochs=20):
    w1, w2, b = 0.0, 0.0, 0.0

    for ep in range(1, epochs + 1):
        errors = 0

        for i in range(len(X)):
            x1, x2 = X[i]
            target = T[i]

            y = step(w1 * x1 + w2 * x2 + b)
            e = target - y

            if e != 0:
                w1 += lr * e * x1
                w2 += lr * e * x2
                b += lr * e
                errors += 1

        print(
            "Epoch", ep,
            "| Weights:", round(w1, 2), round(w2, 2),
            "| Bias:", round(b, 2),
            "| Errors:", errors
        )

        if errors == 0:
            break

    return w1, w2, b


def test(X, T, w1, w2, b):
    print("\nX1 X2 | Target | Output")

    for i in range(len(X)):
        x1, x2 = X[i]
        y = step(w1 * x1 + w2 * x2 + b)

        print(x1, x2, " | ", T[i], " | ", y)


# Input data
X = [(0, 0), (0, 1), (1, 0), (1, 1)]


# AND Gate
print("=== AND GATE ===")
T = [0, 0, 0, 1]

w1, w2, b = train(X, T)
test(X, T, w1, w2, b)


# OR Gate
print("\n=== OR GATE ===")
T = [0, 1, 1, 1]

w1, w2, b = train(X, T)
test(X, T, w1, w2, b)


# XOR Gate
print("\n=== XOR GATE ===")
T = [0, 1, 1, 0]

w1, w2, b = train(X, T, epochs=10)
test(X, T, w1, w2, b)


# ============================================================
# EXPERIMENT 5: SUPERVISED LEARNING USING K-NEAREST NEIGHBOURS
# ============================================================

import random
import math


# 1. Dataset: [Hours, Attendance, Marks, Result]
# Result: 0 = Fail, 1 = Pass
data = [
    [1, 45, 35, 0],
    [2, 50, 40, 0],
    [3, 55, 45, 0],
    [4, 62, 48, 0],
    [2, 40, 38, 0],
    [3, 48, 42, 0],
    [5, 52, 44, 0],
    [4, 45, 40, 0],
    [2, 58, 50, 0],
    [3, 65, 52, 0],
    [6, 75, 60, 1],
    [7, 80, 65, 1],
    [5, 85, 58, 1],
    [8, 90, 70, 1],
    [6, 70, 62, 1],
    [7, 88, 72, 1],
    [9, 92, 78, 1],
    [5, 78, 66, 1],
    [8, 82, 68, 1],
    [6, 95, 75, 1]
]


# 2. Split into training and testing data
random.shuffle(data)

train = data[:15]
test = data[15:]


# 3. Calculate Euclidean distance
def distance(a, b):
    total = 0

    for i in range(3):
        total += (a[i] - b[i]) ** 2

    return math.sqrt(total)


# 4. Predict using KNN (K = 3)
def predict(student):
    distances = []

    for row in train:
        d = distance(student, row)
        result = row[3]

        distances.append([d, result])

    distances.sort()

    # Take the 3 nearest neighbours
    pass_votes = 0

    for i in range(3):
        if distances[i][1] == 1:
            pass_votes += 1

    if pass_votes >= 2:
        return 1
    else:
        return 0


# 5. Test the model
correct = 0

print("Actual | Predicted")

for student in test:
    actual = student[3]
    predicted = predict(student)

    print(" ", actual, " | ", predicted)

    if actual == predicted:
        correct += 1


# 6. Calculate accuracy
accuracy = correct / len(test) * 100
print("Accuracy:", accuracy, "%")


# 7. Predict for a new student
new_student = [6, 80, 65]
result = predict(new_student)

if result == 1:
    print("New Student: PASS")
else:
    print("New Student: FAIL")


# ============================================================
# EXPERIMENT 6: UNSUPERVISED LEARNING USING K-MEANS CLUSTERING
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Dataset: [Hours studied, Marks]
X = np.array([
    [1, 20],
    [2, 25],
    [3, 30],
    [6, 65],
    [7, 70],
    [8, 75],
    [4, 40],
    [5, 45],
    [9, 90]
])


# K-Means clustering
model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(X)


# Display clusters
print("Cluster Labels:", model.labels_)
print("Centroids:", model.cluster_centers_)


# Predict new data
new = np.array([[5, 50]])
print("New Data Cluster:", model.predict(new))


# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=model.labels_)
plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    marker='X',
    s=200,
    color='red'
)

plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("K-Means Clustering")
plt.show()


# ============================================================
# EXPERIMENT 7: ASSOCIATIVE MEMORY NETWORKS
# ============================================================

import numpy as np


def sign(x):
    return np.where(x >= 0, 1, -1)


# 1. AUTO-ASSOCIATIVE MEMORY
X = np.array([
    [1, -1, 1],
    [-1, 1, -1]
])

W = X.T @ X
np.fill_diagonal(W, 0)

input_pattern = np.array([1, -1, -1])

print("Auto Associative:", sign(W @ input_pattern))


# 2. HETERO-ASSOCIATIVE MEMORY
X = np.array([
    [1, -1],
    [-1, 1]
])

Y = np.array([
    [1, 1],
    [-1, -1]
])

W = X.T @ Y
input_pattern = np.array([1, -1])

print("Hetero Associative:", sign(input_pattern @ W))


# 3. BIDIRECTIONAL ASSOCIATIVE MEMORY (BAM)
W = X.T @ Y
x = np.array([1, -1])

for i in range(5):
    y = sign(x @ W)
    x = sign(y @ W.T)

print("BAM Output:", y)
print("BAM Input:", x)


# 4. HOPFIELD NETWORK
X = np.array([
    [1, -1, 1],
    [-1, 1, -1]
])

W = X.T @ X
np.fill_diagonal(W, 0)

state = np.array([1, -1, -1])

for i in range(5):
    for j in range(len(state)):
        state[j] = sign(W[j] @ state)

print("Hopfield Output:", state)


# ============================================================
# EXPERIMENT 8: FUZZY SETS AND FUZZY RELATIONS
# ============================================================

import numpy as np
import matplotlib.pyplot as plt


# 1. Membership Functions
def triangle(x, a, b, c):
    return max(0, min((x - a) / (b - a), (c - x) / (c - b)))


def trapezoid(x, a, b, c, d):
    return max(0, min((x - a) / (b - a), 1, (d - x) / (d - c)))


# 2. Temperature and Fuzzy Sets
T = np.arange(10, 41, 5)

cold = [trapezoid(x, 5, 10, 15, 25) for x in T]
warm = [triangle(x, 15, 25, 35) for x in T]
hot = [trapezoid(x, 25, 35, 40, 45) for x in T]


# 3. User Input and Membership Values
temp = float(input("Enter temperature: "))

print("\nMembership Values:")
print("Cold:", round(trapezoid(temp, 5, 10, 15, 25), 2))
print("Warm:", round(triangle(temp, 15, 25, 35), 2))
print("Hot :", round(trapezoid(temp, 25, 35, 40, 45), 2))


# 4. Fuzzy Set Operations
print("\nUnion:", np.maximum(warm, hot))
print("Intersection:", np.minimum(warm, hot))
print("Complement:", 1 - np.array(warm))


# 5. Alpha Cut
alpha = 0.5
print("\nAlpha Cut:", T[np.array(warm) >= alpha])


# 6. Fuzzy Relation Composition (Max-Min)
R1 = np.array([
    [0.2, 0.5, 0.7],
    [0.7, 0.6, 0.2]
])

R2 = np.array([
    [0.1, 0.5],
    [0.6, 0.3],
    [0.8, 0.9]
])

R = np.zeros((2, 2))

for i in range(2):
    for j in range(2):
        values = []

        for k in range(3):
            values.append(min(R1[i, k], R2[k, j]))

        R[i, j] = max(values)

print("\nMax-Min Composition:")
print(R)


# 7. Extension Principle (y = x²)
D = {
    -2: 0.3,
    -1: 0.6,
    0: 1.0,
    1: 0.8,
    2: 0.5
}

Y = {}

for x in D:
    y = x ** 2
    Y[y] = max(Y.get(y, 0), D[x])

print("\nExtension Principle:")
print(Y)


# 8. Plot Fuzzy Sets
plt.plot(T, cold, marker='o', label="Cold")
plt.plot(T, warm, marker='o', label="Warm")
plt.plot(T, hot, marker='o', label="Hot")

plt.xlabel("Temperature (°C)")
plt.ylabel("Membership Value")
plt.title("Greenhouse Fuzzy Sets")
plt.legend()
plt.grid()
plt.show()


# ============================================================
# EXPERIMENT 9: FUZZY LOGIC CONTROLLER
# ============================================================

import numpy as np


# 1. Triangular Membership Function
def trimf(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif x == b:
        return 1
    elif x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)


# 2. Membership Functions
E = {
    'N': (-10, -10, 0),
    'Z': (-10, 0, 10),
    'P': (0, 10, 10)
}

DE = {
    'N': (-5, -5, 0),
    'Z': (-5, 0, 5),
    'P': (0, 5, 5)
}

U = {
    'Cooling': (-100, -100, 0),
    'Maintain': (-100, 0, 100),
    'Heating': (0, 100, 100)
}


# 3. Fuzzy Rules
rules = [
    ('N', 'N', 'Cooling'),
    ('N', 'Z', 'Cooling'),
    ('N', 'P', 'Maintain'),
    ('Z', 'N', 'Cooling'),
    ('Z', 'Z', 'Maintain'),
    ('Z', 'P', 'Heating'),
    ('P', 'N', 'Maintain'),
    ('P', 'Z', 'Heating'),
    ('P', 'P', 'Heating')
]


# 4. Fuzzification
def fuzzify(x, sets):
    result = {}

    for k in sets:
        a, b, c = sets[k]
        result[k] = trimf(x, a, b, c)

    return result


# 5. Fuzzy Controller
def controller(e, de):
    E1 = fuzzify(e, E)
    E2 = fuzzify(de, DE)

    u = np.arange(-100, 101)
    agg = np.zeros(len(u))

    for a, b, out in rules:
        strength = min(E1[a], E2[b])

        for i in range(len(u)):
            mf = trimf(u[i], *U[out])
            agg[i] = max(agg[i], min(strength, mf))

    if np.sum(agg) == 0:
        return 0

    return np.sum(u * agg) / np.sum(agg)


# 6. User Inputs
desired = 24

actual = float(input("Enter actual temperature: "))
previous = float(input("Enter previous temperature: "))

error = desired - actual
change = error - (desired - previous)


# 7. Calculate Output
output = controller(error, change)

print("\nTemperature Error:", error)
print("Change in Error:", change)
print("Control Output:", round(output, 2))

if output > 1:
    print("Action: HEATING")
elif output < -1:
    print("Action: COOLING")
else:
    print("Action: MAINTAIN")
