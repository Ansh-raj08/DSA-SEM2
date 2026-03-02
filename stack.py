class stack:
    def __init__(self,myCapacity):
        self.top =-1
        self.capacity = myCapacity
        self.stackArray = [None]*myCapacity

    def push(self,myData):
        if self.top == self.capacity-1:
            print("Stack overflow")
            return
        self.top += 1
        self.stackArray[self.top] = myData

    def pop(self):
        if self.top == -1:
            print("stack underflow")
            return

        value = self.stackArray[self.top]
        self.stackArray[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            return
        
        return self.stackArray[self.top]
    
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    
    def isFull(self):
        if self.top == self.capacity - 1:
            return True
        return False

    def contents(self):
        # Return a snapshot of the active stack elements from bottom to top.
        return self.stackArray[: self.top + 1]
    
myStack = stack(5)
print(myStack.isEmpty())
print(myStack.isFull())
myStack.push(10)
myStack.push(15)
print(myStack.peek())
print("popped data: " , myStack.pop())
print("popped data: " , myStack.pop())

# Push five numbers after popping
for value in [2, 4, 6, 8, 10]:
    myStack.push(value)
    print(f"pushed: {value}")

print("top after pushes:", myStack.peek())
print("is stack full now?", myStack.isFull())
print("current stack:", myStack.contents())