import random, copy

def neighbor(f, x, h):
    x += random.uniform(-h, h)
    return f(x), x

def hillClimbing(f, x, h = 0.001):
    if f(x) <= 0:
        print("请更换初始值，使多项式结果大于 0")
        return

    failCount = 0

    while (failCount < 10000):
        fnow = f(x)
        fneighbor, newx = neighbor(f, copy.copy(x), h)

        if fneighbor < fnow:
            if fneighbor <= 0:
                break

            x = newx
            print("x=", x, "f(x)=", fneighbor)
            failCount = 0
        else:
            failCount = failCount + 1
    else:
        print("无实数解")

def f(x):
    return x**5 + 1

hillClimbing(f, 0)
