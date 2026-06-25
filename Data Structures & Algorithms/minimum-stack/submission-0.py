class MinStack:

    def __init__(self):
        self.stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]
        while len(self.stack):
            val = self.stack.pop()      
            mini = min(val, mini)
            tmp.append(val)              
        while len(tmp):
            self.stack.append(tmp.pop()) 
        return mini