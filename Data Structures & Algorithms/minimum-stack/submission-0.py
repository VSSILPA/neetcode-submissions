class MinStack:

    def __init__(self):
        self.output = []
        

    def push(self, val: int) -> None:
        self.output.append(val)
        

    def pop(self) -> None:
        self.output.pop()
        

    def top(self) -> int:
        return self.output[-1]
        

    def getMin(self) -> int:
        return min(self.output)
        
