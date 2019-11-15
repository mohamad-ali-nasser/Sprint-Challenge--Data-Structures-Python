class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        n = 0
        if item == None:
            return
        if None in self.storage:
            for i in self.storage:
                if i != None:
                    n +=1
            print(self.storage)
            del self.storage[n]
            print(self.storage)
            self.storage.insert(n, item)
            # self.current += 1
            
        else:
            del self.storage[self.current]
            self.storage.insert(self.current,item)
            self.current += 1
            if self.current == self.capacity:
                self.current = 0

    def get(self):
        some_list = []
        # if self.current == 0:
        #     return []
        for i in self.storage:
            if i:
                some_list.append(i)
        # if len(some_list) == 0:
        #     return some_list
        return some_list
