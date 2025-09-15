import numpy as np

# --------- 1. Input and Output (OR gate) ----------
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])   # Inputs
y = np.array([[0],
              [1],
              [1],
              [1]])     # Output of OR gate

# --------- 2. Initialize weights and biases ----------
np.random.seed(42)
weights = np.random.rand(2, 1)   # 2 inputs -> 1 output neuron
bias = np.random.rand(1)

# --------- 3. Define Activation Function (Sigmoid) ----------
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# --------- 4. Forward Pass ----------
z = np.dot(X, weights) + bias
output = sigmoid(z)

print("Input:\n", X)
print("\nInitial Weights:\n", weights)
print("\nBias:\n", bias)
print("\nOutput after Feedforward:\n", output)
