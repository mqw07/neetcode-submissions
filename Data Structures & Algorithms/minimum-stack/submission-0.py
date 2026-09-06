import math

class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = [math.inf]
       
    def push(self, val: int) -> None:
        self.stk.append(val)
        self.minstk.append(min(self.minstk[-1], val))

    def pop(self) -> None:
        val = self.stk.pop()
        self.minstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
        
