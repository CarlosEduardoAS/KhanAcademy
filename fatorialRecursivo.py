def fatorial(n):
    if n < 1:
        return 1
    else:
        return n * fatorial(n - 1)


f = fatorial(5)
print(f)
