class MyStack:

    def __init__(self) -> None:
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push an element onto the stack.
        
        Args:
        x (int): The element to push onto the stack.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Remove the top element from the stack and return it.
        
        Returns:
        int: The top element of the stack.
        """
        if not self.empty():
            top_element = self.stack[-1]
            self.stack = self.stack[:-1]
            return top_element
        else:
            raise IndexError("Pop from empty stack")

    def top(self) -> int:
        """
        Get the top element of the stack without removing it.
        
        Returns:
        int: The top element of the stack.
        """
        if not self.empty():
            return self.stack[-1] 
        else:
            raise IndexError("Top from empty stack")

    def empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
        bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0 


# Test cases
stack = MyStack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.top())  # Output: Top element: 30
print("Popped element:", stack.pop())  # Output: Popped element: 30
print("Is stack empty?", stack.empty())  # Output: Is stack empty? False
print("Top element:", stack.top())  # Output: Top element: 20
stack.pop()
stack.pop()
print("Is stack empty after popping all elements?",
      stack.empty())  # Output: True
