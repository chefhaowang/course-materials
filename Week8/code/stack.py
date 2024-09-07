class MyStack:

    def __init__(self) -> None:
        pass

    def push(self, x: int) -> None:
        """
        Push an element onto the stack.
        """
        pass

    def pop(self) -> int:
        """
        Remove the top element from the stack and return it.
        """
        pass

    def top(self) -> int:
        """
        Get the top element of the stack without removing it.
        """
        pass

    def empty(self) -> bool:
        """
        Check if the stack is empty.
        """
        pass


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
