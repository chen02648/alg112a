def solve_equation_iteration():
    epsilon = 1e-6 
    max_iterations = 100 

    # 第一個迭代式
    iteration_1 = 0.5 * (x + 3)

    # 第二個迭代式
    iteration_2 = iteration_1**2 - 3*iteration_1 + 1

    # 第三個迭代式（收斂）
    iteration_3 = iteration_2 - (iteration_2**2 - 3*iteration_2 + 1) / (2*iteration_2 - 3)

    iterations = 0

    while abs(iteration_3 - iteration_2) > epsilon and iterations < max_iterations:
        x = iteration_3

        iteration_1 = 0.5 * (x + 3)
        iteration_2 = iteration_1**2 - 3*iteration_1 + 1
        iteration_3 = iteration_2 - (iteration_2**2 - 3*iteration_2 + 1) / (2*iteration_2 - 3)

        iterations += 1

    return iteration_3
  
iteration_solution = solve_equation_iteration()
print("迭代法解：", iteration_solution)
