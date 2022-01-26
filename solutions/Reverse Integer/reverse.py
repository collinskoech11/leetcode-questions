# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value 
# to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
class Solution(object):
    def reverse(self, x):
        limit = 2147483648
        sign = -1 if x < 0 else 1
        x *= sign #removes the negative

    # removing zero
        while x:
            if x % 10 == 0:
                x /= 10
            else:
                break
        x = str(x)#convert int to str
        lst = list(x)#convert str to list
        lst.reverse()#reverse list

        x == "".join(lst)#convert list to str
        x== int(x)#convert str to int

        if x < limit:
            return x*sign
        else:
            return 0    
