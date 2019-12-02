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

        hash_value = 5381

        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + char
        return hash_value
        


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
        #testing to resize at 70% capacity
        # if self.count >= self.capacity * .7:
        #     self.resize()


        #setting index to the hashed value of the key
        index = self._hash_mod(key)

        #setting pair equal to that position in the array
        pair = self.storage[index]

        #create a new variable and set it to None -- this will be the inserted value
        final_pair = None
               
           
        #if that index position it was set to is NOT None (a collision occurs)
        #shift everything to the right
        while pair is not None and pair.key != key:
            final_pair = pair #set final pair == to the pair (the item you're trying to insert)
            pair = final_pair.next # then set pair == to the node next to final pair


        #If index position is None and available for placement
        #create new pair variable and create a node with the key and value passed in
        new_pair = LinkedPair(key, value)
      

        #create a Linked List of nodes 
        #place the node inside the created linked list using .next(self.next is always None)
        new_pair.next = self.storage[index]

        #set that index position == to the node at new pair
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
        
        #set index to the hash
        index = self._hash_mod(key)

        #set the cur variable to the current index
        cur = self.storage[index]

        #set prev to None
        prev = None
    
        #while the current index is not None and it is not the key you are looking for, traverse the list
        while cur is not None and cur.key != key:
            prev = cur #set previous to current
            cur = prev.next #set current to the next node
        if cur is None: #if current == None, Node does not exist
            print('Error: No node to remove')
        else: # while loop ended, cur is not None, so cur.key must == key (the node we are looking for)
            if prev is None: #if None, it is the first item in the list
                self.storage[index] = cur.next #set the index to the next node
            else:
                prev.next = cur.next # skip over item
            
            
    


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''


        index = self._hash_mod(key)
        pair = self.storage[index]
        
        #checking that index and then traversing through the LL at that position
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

        self.capacity *= 2 #resizing hashtable by two
        new_storage = HashTable(self.capacity) #set new storage = to a created hashtable with that capacity
        for node in self.storage: #go through and copy each item in the new table
            current = node
            while current is not None:
                new_storage.insert(current.key, current.value)
                current = current.next
        #self = new_storage # Would this work?
        self.storage = new_storage.storage
        # self.capacity = new_storage.capacity
        

def resize(self, factor=2):
        """
        Resizes the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        """
        self.capacity = int(self.capacity * factor)
        new_storage = [None] * self.capacity
        for x in self.storage:
            if x:
                node = x
                index = self._hash_mod(node.key)
                new_storage[index] = LinkedPair(node.key, node.value)
                while node.next:
                    node = node.next
                    index = self._hash_mod(node.key)
                    new_storage[index] = LinkedPair(node.key, node.value)
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