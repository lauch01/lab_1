#ejercicio2 
def inverted(n):
    inv=0
    ult_n=0
    while n>0: 
        ult_n=inv%10
        inverted=inverted*10+ult_n
        n//=10
        return (inverted)
    