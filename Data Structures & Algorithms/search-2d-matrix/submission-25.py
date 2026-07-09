class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        m = (l + r) // 2

        while l <= r:
            if matrix[m][0] < target:
                if matrix[m][-1] > target:
                    break
                elif matrix[m][-1] == target:
                    return True
                
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] == target:
                return True
            
            m = (l + r) // 2
        
        ll, rr = 0, len(matrix[0]) - 1
        mm = (ll + rr) // 2

        while ll <= rr:
            if matrix[m][mm] < target:
                ll = mm + 1
            elif matrix[m][mm] > target:
                rr = mm - 1
            elif matrix[m][mm] == target:
                return True
            mm = (ll + rr) // 2
        
        return False
