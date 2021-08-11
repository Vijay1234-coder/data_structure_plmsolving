class HashTable:
    # create e,pty bucket list of given size
    def __init__(self,size):
        self.size=size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Insert values into hash map

    def set_val(self,key,val):
        # Get the index from the  key
        # using hash function
        hashed_key= hash(key) % self.size
        # Get the bucket corresponding to index

        bucket = self.hash_table[hashed_key]
        found_key =False





h=HashTable(5)
print(h.create_buckets())
print(h.set_val(2,3))


