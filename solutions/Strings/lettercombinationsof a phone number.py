class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup ={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        if not digits: return []
        output = [""]
        for digit in digits:
            tmp=[]
            for value in lookup[digit]:
                for o in output:
                    tmp.append(o+value)
            output = tmp
        return output
