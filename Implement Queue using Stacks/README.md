LeetCode 232 - Implement Queue using Stacks
📜 Problem Statement
LeetCode Problem 232 asks to implement a queue using two stacks. The challenge is to create a queue that supports the following operations:

push(x): Push element x to the back of the queue.

pop(): Removes the element from the front of the queue.

peek(): Get the front element.

empty(): Return whether the queue is empty.

👨‍💻 Objective
You need to implement these operations in a way that mimics the behavior of a queue, while only using two stacks. Stacks, as you may know, follow the Last In First Out (LIFO) principle, but you need to simulate the First In First Out (FIFO) behavior of a queue.

⚡️ Approach
The main trick here is to leverage the stacks' LIFO property while simulating the FIFO behavior of a queue. This is achieved using the following two-stack strategy:

Stack1 (stack1): Used for push operations.

Stack2 (stack2): Used for pop and peek operations.

Transfer Method
When we pop or peek, we move the elements from stack1 to stack2. This is done because the elements in stack1 are inserted in reverse order, but we need to retrieve them in the same order for FIFO. By transferring the elements to stack2, we maintain the original order for retrieval.

🔄 Operations
1. push(x)
This method pushes an element to the back of the queue. It is done simply by appending the element to stack1.

python
Copy
Edit
    def push(self, x: int) -> None:
        self.stack1.append(x)
2. pop()
This method removes the front element of the queue. If stack2 is empty, it transfers all elements from stack1 to stack2 (this ensures that the front element is at the top of stack2). After transferring, we pop the top element from stack2.

python
Copy
Edit
    def pop(self) -> int:
        self.transfer()
        return self.stack2.pop()
3. peek()
This method gets the front element without removing it. Again, we ensure that the elements in stack2 are in the correct order by transferring from stack1 if necessary.

python
Copy
Edit
    def peek(self) -> int:
        self.transfer()
        return self.stack2[-1]
4. empty()
This method checks whether the queue is empty by checking if both stack1 and stack2 are empty.

python
Copy
Edit
    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0
5. transfer()
The transfer method is used internally to move elements from stack1 to stack2 only when stack2 is empty. This method ensures that elements are transferred in the correct order to maintain FIFO behavior.

python
Copy
Edit
    def transfer(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
⏰ Time Complexity
push(x): O(1) – We only append an element to stack1.

pop(): O(n) in the worst case – If stack2 is empty, all elements from stack1 are moved to stack2.

peek(): O(n) in the worst case – Similar to pop, we might need to transfer elements before accessing the top of stack2.

empty(): O(1) – Simply checks the lengths of both stacks.

💾 Space Complexity
O(n) – We use two stacks to hold all the elements.

📝 Code
python
Copy
Edit
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.transfer()
        return self.stack2.pop()

    def peek(self) -> int:
        self.transfer()
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def transfer(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
🧑‍💻 Example Usage
python
Copy
Edit
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.pop())  # Output: 1
print(obj.peek()) # Output: 2
print(obj.empty())  # Output: False
🎯 Conclusion
This approach cleverly uses the stack properties to simulate a queue. While the time complexity for pop() and peek() might not be constant in the worst case, this solution offers an elegant and space-efficient way to implement a queue using stacks.

