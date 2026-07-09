class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for par in s:
            if par == '(' or par == '{' or par == '[':
                st.append(par)
            else:
                if len(st) == 0:
                    return False
                match = st.pop()
                if match == '(' and par == ')':
                    continue
                elif match == '{' and par == '}':
                    continue
                elif match == '[' and par == ']':
                    continue
                else:
                    return False
        
        return not st
