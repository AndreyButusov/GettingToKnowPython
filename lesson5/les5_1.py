# Задача 1.  Написать последовательность Фибоначи через рекурсию


def fibonacci(N):
    if N <= 1:
        return N
    return fibonacci(N - 1) + fibonacci(N - 2)

for i in range(10):
    print(fibonacci(i), end=" ")

#print(fibonacci(7))