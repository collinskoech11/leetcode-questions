class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        turtle = hare = nums[0] #initialise two pointers at the beginning of the list
        turtle = nums[turtle] #moves one position
        hare = nums[nums[hare]] #moves two positions
        
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[nums[hare]]
        turtle = nums[0]
        
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[hare]
        return turtle
