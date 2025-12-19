import numpy as np 

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