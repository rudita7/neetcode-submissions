class MinStack:

    def __init__(self):
        self.arr = []
        self.saved = []
    def push(self, val: int) -> None:
        if self.arr:
            if val <= self.saved[-1]:

                self.saved.append(val)
        elif not self.arr:
            self.saved.append(val)
        self.arr.append(val)


    def pop(self) -> None:
        if self.arr:
            s= self.arr.pop()
        if s == self.saved[-1]:
            self.saved.pop()

    def top(self) -> int:
        if self.arr:

            return self.arr[-1]

    def getMin(self) -> int:
        return self.saved[-1]

