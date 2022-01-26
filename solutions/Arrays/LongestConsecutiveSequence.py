class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #first solution which is not the optimal solution since it dos not run in 0(n) time
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        #keep track of lengths sofar and the final output
        sofar = 1
        output = 1
        for i in range(1,len(nums)):
            if nums[i-1]+1 == nums[i]:
                sofar +=1
            else:
                sofar =1
            output=max(output,sofar)
        return output
        
        
        #second solution 
        nums = set(nums)
        output = 0
        
        for n in nums:
            if n-1 not in nums:
                start = n
                while start in nums:
                    start+=1
                output=max(output,start-n)
        return output
                
                
                
                
            
            
    
        
        
