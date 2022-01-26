class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #solve it iteratively
        output = [[]]
        for n in nums:
            output += [ o + [n] for o in output]
        return output
            
