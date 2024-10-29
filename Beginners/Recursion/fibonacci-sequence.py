# 0 1 2 3 4 5 6  7
# 0 1 1 2 3 5 8 13

def fibonacciRecursion(num):
    if num < 2:
        return num
    else:
        return fibonacciRecursion(num-2) + fibonacciRecursion(num-1)
    
def fibonaccilIteration(num):
    if num < 2:
        return num
    
    i, j = 0, 1
    for _ in range(2,num + 1):
        temp = i + j
        i = j
        j = temp
    return j;

def testCase(fib, expected, func):
    actual = func(fib)
    if actual == expected:
        print(f"Fib({fib})={expected} - passed")
    else:
        print(f"Fib({fib}) return {actual}, expected {expected} - failed")

testCase(4, 3, fibonacciRecursion);
testCase(4, 3, fibonaccilIteration);
    

