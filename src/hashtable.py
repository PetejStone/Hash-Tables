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
        self.count = 0
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
        # if cur.key == key and cur.next is not None:
        #     cur = cur.next
        # elif cur.key == key:
        #     cur = None
        # print(f'Current next: {cur.next.value}')
        # if cur is None:
        #     print('Error')
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
            
            
        # elif cur.key == key:
        #     prev.next = None
        #     cur = None
        # cur = cur.next
       
    #     '''
    #     Find and remove the node with the given value
    #     '''
    # # If we have no head
    #     if not self.head:
    #         # print an error and return
    #         print('Error: value not found')
    #     # If the head has our value
    #     elif self.head.value == value:
    #         # Remove the head by pointing self.head to head.next
    #         self.head = self.head.next
    #     # Else 
    #     else:
    #         # Keep track of parent node
    #         parent = self.head
    #         current = self.head.next
    #         # walk through the linked list until we find a matching value
    #         while current:
    #             if current.value == value:
    #                 # Delete the node by pointing parent.next to node.next
    #                 parent.next = current.next
    #                 return
    #             parent = parent.next
    #             current = current.next
    #                 # return

        # # If we find a matching value, point parent.next to node.next
        # # If we get to the end and have not foud the value, print error
        # print('Error: Value not found')



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
        #double size
        self.capacity *= 2
        new_storage = [None] * self.capacity

        #copy old
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage


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