class MyHashSet:

    def __init__(self):
        self.size = 769  # prime number to reduce collisions
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        i = self._hash(key)
        bucket = self.buckets[i]
        for v in bucket:
            if v == key:
                return  # already present
        bucket.append(key)

    def remove(self, key: int) -> None:
        i = self._hash(key)
        bucket = self.buckets[i]
        for idx, v in enumerate(bucket):
            if v == key:
                bucket.pop(idx)
                return

    def contains(self, key: int) -> bool:
        i = self._hash(key)
        bucket = self.buckets[i]
        for v in bucket:
            if v == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)