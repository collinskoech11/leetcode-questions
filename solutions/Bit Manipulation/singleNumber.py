    def singleNumber(self, nums: List[int]) -> int:
        #solution 1
        c = Counter(nums)
        for num in c:
            if c[num] == 1:
                return num
        
        
        #solution2
        a = 0 
        for i in nums:
            a^= i
            return a
