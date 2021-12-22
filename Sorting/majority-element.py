"""given an array nums return the majority element
example nums=[2,2,3,2,2]
returns 2
"""
class Solution:
    def majorityElement(self, nums:List[int]) -> int:
        c = Counter(nums)
        return max(c)
