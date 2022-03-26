class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # it is possible to do the conversion only if m*n == original
        L = len(original)
        if m*n != L:
            return []
        ans = []
        
        #for that given row append the elements 
        #do it one row at a time
        for i in range(m):
            ans.append(original[i*n : n*i + n])
        return ans
