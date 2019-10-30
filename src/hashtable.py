# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = capacity
        self.head = None

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''


        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''

        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
      
        index = self._hash_mod(key)
        # print(f'index: {index}')
        #if storage is full
        pair = self.storage[index]
        final_pair = None
        ##insert a word 'for'
        #index is 62
         #  fp      p
        #checking for multiple pairs, two have same index
       
        # self.count += 1
        while pair is not None and pair.key != key:
            final_pair = pair
            pair = final_pair.next
      
        new_pair = LinkedPair(key, value)
        new_pair.next = self.storage[index]
        self.storage[index] = new_pair
        

        # if self.count >= self.capacity:
        #     return self.resize()
            
        #shift everything to right
        #start from end and go backwards to prevent overriding values
        # for i in range(self.count, index, -1):
        #     self.storage[i] = self.storage[i-1]

            

        #insert value
        # self.storage[index] = LinkedPair(key,value)
        # print(f'Item: {self.storage[index].value}')
        # self.count += 1



    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        # p         
      #  1   2   3
        
        index = self._hash_mod(key)
        cur = self.storage[index]
        prev = None
   
        while cur is not None and cur.key != key:
            prev = cur
            cur = prev.next
        if cur is None:
            print('Error: No node to remove')
        else:
            if prev is None:
                # cur.next = self.storage[index]
                self.storage[index] = cur.next
            else:
                prev.next = cur.next
            
            
    


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        
        while pair is not None:
            if pair.key == key:
                return pair.value
            pair = pair.next


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''

        self.capacity *= 2
        new_storage = HashTable(self.capacity)
        for node in self.storage:
            current = node
            while current is not None:
                new_storage.insert(current.key, current.value)
                current = current.next
        #self = new_storage # Would this work?
        self.storage = new_storage.storage
        # self.capacity = new_storage.capacity
        


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")