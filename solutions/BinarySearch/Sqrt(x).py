class Solution:
    def mySqrt(self, x: int) -> int:
        # step 1: find the square root without built-in operators
        # step 2: if the answer is a decimal truncate it
        return int(math.sqrt(x))
