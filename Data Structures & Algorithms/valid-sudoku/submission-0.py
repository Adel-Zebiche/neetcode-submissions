class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rule1
        n = len(board)
        nb = set("123456789")
        for row in board :
            seen = set()
            for elt in row :
                if elt in nb :
                    if elt not in seen :
                        seen.add(elt)
                    else :
                        return False
        #rule2
        for i in range(n) :
            seen = set()
            for j in range(n) :
                elt = board[j][i]
                if elt in nb :
                    if elt not in seen :
                        seen.add(elt)
                    else :
                        return False
        #rule3
        couples = [(0,0), (0,3), (0,6),
                   (3,0), (3,3), (3,6),
                   (6,0), (6,3), (6,6)]
        for (i,j) in couples :
            seen = set()
            for idx in range(i, i+3) :
                for jdx in range(j, j+3) :
                    elt = board[idx][jdx]
                    if elt in nb :
                        if elt in seen :
                            return False
                        seen.add(elt)
        return True





