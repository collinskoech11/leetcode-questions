There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

def sockMerchant(n, ar):
    # Write your code here
    pairs=0
    socks=dict()
    for i in ar:
        if i in socks:
            socks[i] = socks[i]+1
        if i not in socks:
            socks[i] = 1
        if socks[i]%2 ==0:
            pairs+=1
    return pairs
            
        
        
