class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.table[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = self.hash(key)
        bucket = self.table[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        raise KeyError(f"Key '{key}' not found in table.")

    def has(self, key):
        index = self.hash(key)
        bucket = self.table[index]

        for existing_key, _ in bucket:
            if existing_key == key:
                return True

        return False

    def keys(self):
        keys = []
        for bucket in self.table:
            for key, _ in bucket:
                keys.append(key)
        return keys

    def hash(self, key):
        return hash(key) % self.size
