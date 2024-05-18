def f(x):
    x = x ** 2
    if x % 2 != 0:
        return x
    else:
        return False


a = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
b = list(map(f, a))
result = list(filter(f, b))
print(result)
