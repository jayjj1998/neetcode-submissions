class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        m = (l + r) // 2
        count = 0

        while l <= r and count < 10:
            count += 1
            print(f"{l} and {r}")
            if matrix[m][0] < target:
                print("Here")
                if matrix[m][-1] > target:
                    print("HERE")
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
