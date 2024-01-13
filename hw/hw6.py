import numpy as np

# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k, step=1e-6):
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return np.array(gp)


def gradient_descent_optimizer(objective_function, initial_point, learning_rate=0.01, max_iterations=1000, epsilon=1e-6):
    current_point = np.array(initial_point)

    for iteration in range(max_iterations):
        gradient = grad(objective_function, current_point)
        next_point = current_point - learning_rate * gradient

        if np.linalg.norm(next_point - current_point) < epsilon:
            break

        current_point = next_point

    return current_point, objective_function(current_point)


def example_function(p):
    return p[0]**2 + p[1]**2  

initial_point = [1.0, 1.0]
optimal_point, optimal_value = gradient_descent_optimizer(example_function, initial_point)

print("最佳點:", optimal_point)
print("最小值:", optimal_value)
