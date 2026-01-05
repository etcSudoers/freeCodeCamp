def nth_fibonacci(n: int):
    a, b = 0, 1
    for i in range(n):
        #print(a,end=' ')
        if i == n-1: return a
        a, b = b, a + b




assert nth_fibonacci(4) == 2
assert nth_fibonacci(10) == 34
assert nth_fibonacci(15) == 377
assert nth_fibonacci(40) == 63245986
assert nth_fibonacci(75) == 1304969544928657



"""
Nth Fibonacci Number

Given an integer n, return the nth number in the fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. 
The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

"""