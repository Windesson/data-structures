# n! = n * n-1 * 1
# 5! = 5 * (4!) * 1 = 120

def factorialRecursion(num):
    if num == 1:
        return 1
    else:
        return num * factorialRecursion(num -1)

def factorialIteration(num):
    res = 1
    while num > 1:
        res = res * num
        num -=1 
    return res
    
def testCase1(func):
    expected = 120
    actual = func(5)
    if expected == actual:
        print("T1: pass")
    else:
        print(f"T1: failed expected {expected} actual {actual}")

testCase1(factorialRecursion);
testCase1(factorialIteration);