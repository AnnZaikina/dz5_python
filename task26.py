def vozv_stepen (a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        res = a*a
        return res * vozv_stepen(a, b-2)
    
print (vozv_stepen(2, 5))
