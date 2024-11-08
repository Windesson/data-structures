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

def lonelyintegerXOR(arr):
    ans = 0
    for num in arr:
        ans = ans ^ num
    return ans

def lonelyintegerXOR2(arr):
    arr.sort()
    ans = 0
    for num in arr:
        if num == ans:
            ans = 0
        elif ans == 0:
            ans = num
    return ans

print(lonelyintegerXOR([1,1,2,2,0]))
print(lonelyintegerXOR2([1,1,2,2,0]))