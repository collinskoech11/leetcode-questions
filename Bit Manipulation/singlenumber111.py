class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lookup=set()
        for n in nums:
            if n not in lookup:
                lookup.add(n)
            else:
                lookup.remove(n)
        return lookup
