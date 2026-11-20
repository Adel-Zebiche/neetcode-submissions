class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        liste = matrix[0]
        m, n = len(matrix), len(liste)
        for i in range(1, len(matrix)) :
            liste = liste + matrix[i]
        l,r = 0, m*n-1
        while l <= r :
            mid = (l+r)//2
            if liste[mid] > target :
                r = mid-1
            elif liste[mid] < target :
                l = mid+1
            else :
                return True

        return False
