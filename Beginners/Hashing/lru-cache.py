# https://leetcode.com/problems/lru-cache/
class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(None, None), Node(None, None)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}
    
    def remove_node(self, node):
        # _prev, node, _next
        # _prev, _next
        _prev, _next = node.prev, node.next
        _prev.next, _next.prev = _next, _prev

        node.next, node.right = None, None
        del node
        
    def add_node(self, node):
        # _prev, right
        # _prev, node, right
        _prev = self.right.prev
        node.next, node.prev = self.right, _prev
        self.right.prev, _prev.next = node, node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove_node(node)

        new_node = Node(key,node.value)
        self.cache[key] = new_node
        self.add_node(new_node)
        
        return new_node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])

        node = Node(key,value)
        self.add_node(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove_node(self.left.next)

   

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)