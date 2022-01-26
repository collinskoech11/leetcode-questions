# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        result= len(nums)
        for i in range(len(nums)):
            result +=(i - nums[i])
        return result
        
        
        # solution2
        N = len(nums)
        ExpSum = N*(N+1)//2
        ActSum = sum(nums)
        
        return ExpSum- ActSum
