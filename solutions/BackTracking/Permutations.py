class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)#pop the first value off
            perms = self.permute(nums)#get the permutations of the rrmaining values
            for perm in perms:# go through each permutation and add the n that you popped out
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result
