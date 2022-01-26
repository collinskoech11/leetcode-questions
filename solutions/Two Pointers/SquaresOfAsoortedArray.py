class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # if the array is empty return an empty array
        if not nums or len(nums)==0:
            return []
        
        #initialise the pointers
        ans = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        insertLocation = right
        
        #when left pointer is less than right pointer
        while left <= right:
            leftSq = nums[left] * nums[left]
            rightSq = nums[right] * nums[right]
            #squares of the left and right values
            if leftSq <= rightSq:
                ans[insertLocation] = rightSq
                rightSq -=1
                insertLocation -=1
            else:
                ans[insertLocation] = leftSq
                leftSq +=1
                insertLocation +=1
        return ans
