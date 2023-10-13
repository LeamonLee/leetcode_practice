class LRUCache:

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next=None
            self.pre=None

    def __init__(self, capacity: int):
        self.hashMap={}
        self.capacity=capacity
        self.head=None
        self.tail=None

    def get(self, key: int) -> int:
        node = self.hashMap.get(key, None)
        if not node: return -1
        if node != self.tail:
            if node == self.head:
                self.head=self.head.next
            else:
                node.pre.next=node.next
                node.next.pre=node.pre
            
            self.tail.next=node
            node.pre=self.tail
            node.next=None
            self.tail=node
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.hashMap.get(key, None)
        if node:
            node.value=value
            if node != self.tail:
                if node == self.head:
                    self.head=self.head.next
                else:
                    node.pre.next=node.next
                    node.next.pre = node.pre
                self.tail.next=node
                node.pre=self.tail
                node.next=None
                self.tail=node
        else:
            node = self.Node(key, value)
            if self.capacity==0:
                if self.head:
                    temp = self.head
                    if self.head.next:
                        self.head = self.head.next
                    self.hashMap.pop(temp.key, None)
                    self.capacity+=1
            
            if not self.head and not self.tail:
                self.head = node
            else:
                self.tail.next=node
                node.pre=self.tail
                node.next=None
            
            self.tail=node
            self.hashMap[key] = node
            self.capacity-=1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)