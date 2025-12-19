import numpy as np 
import matplotlib.pyplot as plt

m = 100
x = np.linspace(0, 10 , m)
print(x.shape)  # Output: (100,)
noise = np.random.randn(m)

a = 3
b = 2
y = a * x + b + noise
X = np.column_stack((np.ones(m), x))
print(X.shape)  # Output: (100, 2)

def h(X: np.ndarray, theta: np.ndarray) -> np.ndarray:
    return X @ theta

def cost(X: np.ndarray, y: np.ndarray, theta: np.ndarray) -> float:
    return 0.5 * (X @ theta -y).T @ (X @ theta - y)

def gradient(X: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
    return X.T @ (X @ theta - y)

def gradient_descent(X: np.ndarray, y: np.ndarray, theta: np.ndarray, alpha: float, num_iters: int) -> np.ndarray:
    losses = [] 
    for t in range(num_iters):
        theta = theta - alpha * gradient(X, y, theta)
        losses.append(cost(X, y, theta))
        if t % 10 == 0:
            print('theta:', theta)
    return theta, losses

theta_init = np.zeros(2)
theta_final, losses = gradient_descent(X, y, theta_init, alpha=0.0001, num_iters=1000)

plt.plot(losses)
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Convergence of Gradient Descent')
plt.show()