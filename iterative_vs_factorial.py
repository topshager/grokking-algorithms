#iterative
def factI(n):
    result = 1
    while n >  1:
        result = result * n
        n-=1

    return result



#Recurcive
def factR(n):
    if n == 1:
        return n
    else:
        return n *factR(n-1)
