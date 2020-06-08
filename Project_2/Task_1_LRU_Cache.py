class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.counter = 0

class LRU_Cache(object):
 # what happens if I don't do self.capacity
    def __init__(self, capacity):
        self.table = [None]*10000
        self.p = 31
        self.capacity = capacity
        self.entries = 0
        # Initialize class variables
        pass

    def get(self, key):
        bucket_index = self.get_hash_value(key)
        if (self.table[bucket_index] != None):
            if (self.table[bucket_index].key == key):# do this for collisions and if same index
                self.table[bucket_index].counter += 1
                return print("key and value are", self.table[bucket_index].key, self.table[bucket_index].value)
            else: 
                return -1
        else:
            return -1
        
        # Retrieve item from provided key. Return -1 if nonexistent. 
 
    def set(self, key, value):
        bucket_index = self.get_hash_value(key)
        print("bucket index", bucket_index)
        print("current value at bucket_index", self.table[bucket_index])
        print("current entries and current capacity", self.entries, self.capacity)
        print("\n")
        if (self.table[bucket_index] == None):
            if (self.entries < self.capacity):
                self.table[bucket_index] = Node(key,value)
                self.table[bucket_index].counter +=1
                self.entries += 1
                print("entered pair at bucket_index is", self.table[bucket_index].key, self.table[bucket_index].value)
                print("\n")
            else: 
                print("else statement of set function is entered")
                self.remove_old()
                print("completed remove helper function")
                self.table[bucket_index] = Node(key,value)
                self.table[bucket_index].counter +=1
                print("entered pair at bucket_index is", self.table[bucket_index].key, self.table[bucket_index].value)
                self.entries += 1
                print("\n")
         
        
        
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        # what about when key is present in cache ?
        
    def remove_old (self):
        print("\n")
        print("start of remove function")
        old = 1000
        oldest = None
        for x in self.table:        
            if x!= None:     
                index = self.table.index(x)
                print("key,value and counter are", x.key, x.value, x.counter)
                if (x.counter < old):
                    old = x.counter
                    oldest = index
        print("oldest value is", self.table[oldest].key)          
        self.table[oldest] = None
        
        
        
    
        
    def get_hash_value(self, key):
        key = str(key)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            current_coefficient *= self.p     
        return hash_code 
    
    
    
our_cache = LRU_Cache(5)


our_cache.set(1, 1)



our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

print("\n")
#our_cache.set(5, 5) 
#our_cache.set(6, 6)

#our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

