#ex8

#2
def bL(binary):
    binary1 = binary
    decimal, i  = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * 2**i
        binary = binary//10
        i += 1
    print('Decimal equivalent of {} is {}'.format(binary1, decimal))


