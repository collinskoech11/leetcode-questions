class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        for n in nums:
            temp=[]
            for l in ans:
                temp.append(l+[n])
            ans.extend(temp)
        #1.convert the list into  a tuple
        #2.make it a set
        #3.then reconvert it into a list
        return [list(l) for l in set([tuple (l) for l in ans])]
