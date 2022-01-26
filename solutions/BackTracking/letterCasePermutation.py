class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]
        for character in s:
            temp=[]
            if character.isalpha(): #if character is alphanumeric
                for o in output:
                    temp.append(o+character.lower())
                    temp.append(o+character.upper())
            else:# if character is not alphanumeric
                for o in output:
                    temp.append(o+character)
            output = temp
        return output
        
