def dequeue(self, i):
    
    if self.num == 0:
        raise Exception("Queue empty!")
    
    if i < 0 or i >= self.num:
        raise IndexError("Index out of bounds!")
    
    index = (self.first + i) % self.max_size
    item = self.Q[index]
    
    return item