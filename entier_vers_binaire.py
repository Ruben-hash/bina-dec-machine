def entier_vers_binaire(n):
    b = []
    while n > 0:
        b.append(n%2)
        n = n //2
    b.reverse()
    return b






