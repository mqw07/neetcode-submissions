class Solution:
    def isValid(self, s: str) -> bool:
        # ex2: stk = [], [(], [([], [([{]
        #
        #
        if len(s) % 2 != 0:
            return False
        comp = {'(': ')', '[': ']', '{': '}'}
        stk = []

        for st in s:
            if st in comp:
                stk.append(st)
            else:
                if not stk or st != comp[stk.pop()]:
                    return False
        if stk != []:
            return False
        return True
    

