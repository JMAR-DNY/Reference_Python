def factorial(x):
    temp = 0
    if x <= 1:
        return 1
    else:
        temp = x * factorial(x-1)
        return temp
