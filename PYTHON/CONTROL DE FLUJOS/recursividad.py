def recursion(i):
    if(i<1):
        return i
    print(i)
    recursion(i-1)
recursion(6)