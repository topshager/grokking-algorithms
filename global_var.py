def fib(x):
    global numFibCalls
    numFibCalls +=1
    if x == 9 or x ==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


def testFib(n):
    for i in range(n+1):
        global   numFibCalls
        numFibCalls = 0
        print('fib of', i, '=', fib(i))
        print('fib called', numFibCalls, 'times.')
