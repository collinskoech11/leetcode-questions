class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #create an empty array for each s and t
        s_output =[]
        t_output = []
        
        for char in s:#for a character in s
            if char == "#":# if the character is #
                if s_output:
                    s_output.pop()#pop the last edded element from the created array
                else:
                    s_output.append(char)#append value of character into the array
        for char in t:
            if char == "#":
                if t_output:
                    t_output.pop()
                else:
                    t_output.append(char)
                        
        if s_output == t_output:
            return True
        else:
            return False
