
map = { 
        '}':'{', 
        ')':'(', 
        ']':'['
      }

# Validate Parentheses
def isValid(s):
    memo = []

    for c in s:
        if c in map.keys():
            #must be close parentheses
            if len(memo) == 0:
                return False
            if memo[-1] != map[c]:
                return False
            memo = memo[:-1]
        else:
            memo.append(c)
    return len(memo) == 0;
    

def case1():
    s ='([{}])'
    expected = True
    actual = isValid(s)
    if expected == actual:
        print("Test 1: Pass")
    else:
        print("Test 1: Failed")
case1();

def case2():
    s = "[(])"
    expected = False
    actual = isValid(s)
    if expected == actual:
        print("Test 2: Pass")
    else:
        print("Test 2: Failed")
case2();