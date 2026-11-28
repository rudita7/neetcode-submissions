class MinStack:

    def __init__(self):
        self.stack = []
        self. min = float("infinity")
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val
        
    def pop(self) -> None:
        if self.stack:
            top = self.stack.pop()
            if top < 0:
                self.min = self.min - top
            
    def top(self) -> int:
        if self.stack:
            top = self.stack[-1]
            if top > 0:
                top = self.min + top
                return top
            else:
                return self.min

    def getMin(self) -> int:
        return self.min
        
