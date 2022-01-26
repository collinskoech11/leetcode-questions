class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      #use pointers since the space complexity should be o(1)
        leftpointer = 1
        for rightpointer in range(1,len(nums)):
            if nums[rightpointer] != nums[rightpointer-1]:
                nums[leftpointer]=nums[rightpointer]
                leftpointer += 1
        return leftpointer
