import numpy as np
from micrograd import Tensor

# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k):
    p1 = p.copy()
    p1[k] = Tensor(p1[k].data + step)
    return (f(p1) - f(p)) / step

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return np.array([g.data for g in gp])


def gradient_descent_optimizer(objective_function, initial_point, learning_rate=0.01, max_iterations=1000, epsilon=1e-6):
    current_point = [Tensor(x) for x in initial_point]

    for iteration in range(max_iterations):
        gradient = grad(objective_function, current_point)
        next_point = [p - learning_rate * g for p, g in zip(current_point, gradient)]

        if np.linalg.norm(np.array([p.data for p in next_point]) - np.array([p.data for p in current_point])) < epsilon:
            break

        current_point = next_point

    return [p.data for p in current_point], objective_function(current_point)


def example_function(p):
    return p[0]**2 + p[1]**2  

initial_point = [1.0, 1.0]
optimal_point, optimal_value = gradient_descent_optimizer(example_function, initial_point)

print("最佳點:", optimal_point)
print("最小值:", optimal_value)
