#Input: nums = [0,1,2,2,3,0,4,2], val = 2
#Output: 5, nums = [0,1,4,0,3,_,_,_]

def removeElement(val,nums):
    if len(nums) == 0:
        return 0
    else:
        writer, reader = 0, 0
        while reader < len(nums):
            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1 
            reader += 1

        return writer;

def testCase1(): 
    nums = [1,1,1,2,3,4,4,5]
    expectedSize = 5
    removeElement(1,nums)

    #assert
    if nums[:expectedSize] == [2,3,4,4,5]:
        print("pass")
    else:
        raise Exception("failed")

testCase1()