class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return indexOf(nums,target) if target in nums else -1
