#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        return False
    
    # solution2: using hashset
        hashset=set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
