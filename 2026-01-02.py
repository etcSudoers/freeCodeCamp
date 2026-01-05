def nth_fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


nth_fibonacci(10)