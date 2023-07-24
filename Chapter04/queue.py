class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return None
    
    def isEmpty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)