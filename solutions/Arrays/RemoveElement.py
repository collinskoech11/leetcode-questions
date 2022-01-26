class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # given a list and a value, remove the value from the list then return thenumber of the remaining integers in the list
        while nums.count(val):
            nums.remove(val)
