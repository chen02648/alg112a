# 方法 1
def power2n_1(n):
    return 2 ** n

# 方法 2a：用遞迴
def power2n_2x(n):
    if n == 0:
        return 1
    else:
        return power2n_2x(n - 1) * 2

# 方法 2b：用遞迴
def power2n_2y(n):
    if n == 0:
        return 1
    else:
        return 2 * power2n_2y(n - 1)

# 方法 3：用遞迴+查表
def power2n_3z(n, m={}):
    if n == 0:
        return 1
    if n in m:
        return m[n]
    else:
        result = power2n_3z(n - 1, m) * 2
        m[n] = result
        return result

n = int(input("整數 n："))
print(power2n_1(n))
print(power2n_2x(n))
print(power2n_2y(n))
print(power2n_3z(n))
