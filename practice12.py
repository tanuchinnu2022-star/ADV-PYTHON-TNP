class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.order = []
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.pop(0)
            del self.cache[oldest]

        self.cache[key] = value
        self.order.append(key)

# Example
lru = LRUCache(2)
lru.put(1, 10)
lru.put(2, 20)
print(lru.get(1))
lru.put(3, 30)
print(lru.get(2))