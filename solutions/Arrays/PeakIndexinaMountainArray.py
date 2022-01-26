class Solution:
#   solution1
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maxin = arr.index(max(arr))
        return maxin
      
      
#       solution2
        for i in range(len(arr) -1):
            if arr[i] > arr[i+1]:
                return i
            i+=1
