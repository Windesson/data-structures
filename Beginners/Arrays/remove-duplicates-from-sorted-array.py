# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element 
# appears only once. The relative order of the elements 
# should be kept the same. Then return the number of unique 
# elements in nums.
# [1,1,1,2,3,4,4,5]
# strategy: use two pointer, writer and reader starting at index 1.

def removeDuplicates(nums):
    if len(nums) < 2:
        return len(nums)
    
    writer, reader = 1, 1
    while reader < len(nums):
        # ignore duplicated item
        if nums[reader] != nums[writer -1]:
            nums[writer] = nums[reader]
            writer +=1

        reader +=1 

    return writer

def testCase1(): 
    case1 = [1,1,1,2,3,4,4,5]
    expectedSize = 5
    removeDuplicates(case1)

    #assert
    if case1[:expectedSize] == [1,2,3,4,5]:
        print("pass")
    else:
        raise Exception("failed")

testCase1()






