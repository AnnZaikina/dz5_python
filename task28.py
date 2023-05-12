def slozhenie (a,b):
    if a == 1 and b == 1:
        return 2
    if a == 1:
        return 1 + slozhenie (1, b-1)
    if b == 1:
        return 1 + slozhenie (a-1, 1)
    else:
        return 2 + slozhenie(a-1, b-1)
    
print (slozhenie(8, 9))