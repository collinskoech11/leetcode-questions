class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==0 or n ==1:
            return;
        #initialise the left and the right pointer
        left = 0
        right=0
        temp = 0
        while right < n:
            if nums[right] == 0:# if the index at the right pointer is zero, 
                right+=1#move the pointer forward
            else:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                right+=1
                left+=1
