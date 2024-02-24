class CircQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * capacity  # Initialize queue with None values
        self.length = 0
        self.rear = 0
        self.front = 0
        
    def append(self, item):
        if self.is_full():
            raise Exception("The circular queue is full")
        self.queue[self.rear] = item
        self.length += 1
        self.rear = (self.rear + 1) % self.capacity
    
    def is_full(self):
        return self.length == self.capacity
    
    def serve(self):
        if self.length == 0:
            raise Exception("The circular queue is empty")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.length -= 1
        return item
    
    def clear(self):
        self.queue = [None] * self.capacity
        self.front, self.rear = 0, 0

# Example usage:
c = CircQueue(5)
c.append(1)
c.append(2)
c.append(3)
c.append(25)
c.append(36)  # This should raise an exception now

    
        