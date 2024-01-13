def solve_equation_bruteforce():
    solutions = []
    epsilon = 1e-6 

    for x in range(-1000, 1001): 
        equation_result = x**2 - 3*x + 1

        if abs(equation_result) < epsilon:
            solutions.append(x)

    return solutions

bruteforce_solutions = solve_equation_bruteforce()
print("暴力法解：", bruteforce_solutions)
