class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.key_usage = [] # LRU position 0

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value == -1:
            return value

        if key in self.key_usage:
            del self.key_usage[self.key_usage.index(key)]
        self.key_usage.append(key)

        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and self.capacity == len(self.cache):
            del self.cache[self.key_usage[0]]
            del self.key_usage[0]

        self.cache[key] = value
        
        if key in self.key_usage:
            del self.key_usage[self.key_usage.index(key)]
        self.key_usage.append(key)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)