
def reverse(nums):
    print(nums)
    i,j = 0, len(nums) -1
    while i < j:
        nums[i], nums[j] =  nums[j], nums[i]
        i += 1
        j -= 1
    print(nums)

reverse([1,2,3,4,5])