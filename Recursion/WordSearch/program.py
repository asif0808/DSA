def WordSearch(word,board):
    rows=len(board)
    columns=len(board[0])
    path=set()
    def dfs(r,c,i):
        if(i==len(word)):
            return True
        if(c<0 or r<0 or r>=rows or c>=columns or word[i]!=board[r][c] or (r,c) in path):
            return False
        path.add((r,c))
        res=(dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
        path.remove((r,c))
        return res
    for r in range(rows):
        for c in range(columns):
            if(dfs(r,c,0)):
                return True
    return False
print(WordSearch("ABBC",[["A","C","D"],["B","E","A"],["B","G","A"],["C","A","D"]]))