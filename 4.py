
def decbin(n):
    b = [0]
    while n > 0:
        n = n // 2
        if n%2 == 0:
            b.append(0)
        elif n%2 == 1:
            b.append(1)
    b.reverse()
    return b









