#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    memo = dict()
    for num in a:
        memo[num] = memo.get(num, 0) + 1
    for key, val in memo.items():
        if val == 1:
            return key
    return -1