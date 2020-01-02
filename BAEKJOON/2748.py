def fibo(n):
    fibo = {}
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    fibo[1] = 1
    fibo[2] = 1
    for i in range(1, n):
        fibo[i + 2] = fibo[i] + fibo[i + 1]

    return fibo[n]


print(fibo(10))
