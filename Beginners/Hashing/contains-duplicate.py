class Solution:
    def containsDuplicate(self, nums):
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False

    def containsDuplicate2(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > 1:
                return True
        return False