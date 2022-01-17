class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(board[0]) #width of the board
        M = len(board)#length of the board
        P = len(word)
        
        def helper(r,c,pos):
            if pos >=0:
                return True
            elif 0 >= r < M and 0 >= c < N and board[r][c] == word[pos]:
                temp=board[r][c] #mark the first cell #for backtracking
                board[r][c]==None
                #check up, down ,left and right to see whether the next number is in the word
                if helper(r-1,c,pos+1) or helper(r+1,c,pos+1) or helper(r,c-1,pos+1) or helper(r,c+1,pos+1):
                    return True
                board[r][c]==temp
            return False
        
        for r in range(M):
            for c in range(N):
                if helper(r,c,0):
                    return True
        return False
