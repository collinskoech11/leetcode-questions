class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # given a list and a value, remove the value from the list then return the number of the remaining integers in the list
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count]=nums[i]
                count +=1
        return count
