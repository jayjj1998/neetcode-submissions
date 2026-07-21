class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:

        current_day = arr.copy()
        oper_exec = False

        while True:
            for i in range(1, len(arr) - 1):
                if current_day[i - 1] > current_day[i] < current_day[i + 1]:
                    arr[i] += 1
                    oper_exec = True
                elif current_day[i - 1] < current_day[i] > current_day[i + 1]:
                    arr[i] -= 1
                    oper_exec = True
                
            if not oper_exec:
                break

            print (current_day)
            print (arr) 
            current_day = arr.copy()
            oper_exec = False
        
        return arr