TABLE_SIZES=[10, 20, 25, 34, 40, 45]

class HashTable:
    
    def __init__(self, capacity):
        self.n=0
        if capacity is not None:
            self.capacity=capacity
        else:
            self.capacity=TABLE_SIZES[self.n]
        self.keytable=[None]*self.capacity
        self.valuetable=[None]*self.capacity
        
    def is_full(self):
        return len(self.keytable) == self.capacity[self.n] and len(self.valuetable) == self.capacity[self.n]
        
    def hash(self, key):
        return (ord(key)%self.capacity)
    
    def LinearProbe(self, inp):
        while self.keytable[inp] is not None:
            if inp == len(self.keytable)-1:
                return False
            inp+=1
        return inp
    
    def add(self, k, v):
        hashed=hash(k)
        if self.keytable[hashed] is not None:
            self.keytable[hashed]=k
            self.valuetable[hashed]=v
        else:
            h=self.LinearProbe(hashed)
            if h is int:
                self.keytable[h]=k
                self.valuetable[h]=v
            else:
                self.rehash()
            
    def remove(self, key):
        r=hash(key)
        if self.keytable[r] == key:
            self.valuetable = None
        else:
            r=self.LinearProbe(r)
            self.valuetable[r]=None

    def allKeys(self):
        lst=[]
        a=0
        while a<=self.capacity:
            if self.keytable[a] is not None:
                lst.append(self.keytable[a])
        return lst
    
    def allValues(self):
        lst=[]
        a=0
        while a<=self.capacity:
            if self.valuetable[a] is not None:
                lst.append(self.valuetable[a])
        return lst
    
    def value(self, key):
        
    
    def rehash(self):
        key=self.allKeys()
        value=self.allValues()
        self.keytable.clear()
        self.valuetable.clear()
        while len(key) < self.capacity[self.n]:
            self.n+=1
        self.keytable=[None]*self.capacity[self.n]
        self.valuetable=[None]*self.capacity[self.n]
        # Re-add all key-value pairs to the hash table
        for key, value in zip(key, value):
            self.add(key, value)
    
        
            
h=HashTable(25)
h.add(30, 1)


            
            
    
    
    