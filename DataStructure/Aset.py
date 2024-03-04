class Aset:
    def __init__(self):
        self.set=[]
    
    def add(self, item):
        if item not in self.set:
            self.set.append(item)
        return("Same value already exist in the set")
    
    def union(self, set2):
        for x in set2:
            if x not in self.set:
                self.set.append(x)
        return self.set
    
    def intersection(self, set2):
        lst=[]
        if len(self.set) > len(set2):
            pin=self.set
            comp=set2
        else:
            pin=set2
            comp=self.set
        for x in pin:
            if x in comp:
                lst.append(x)
            else:
                return "2 sets doesn't intersect"
        return lst
    
    def length(self):
        return len(self.set)
    
    def display(self):
        for x in self.set:
            print(x)
        
    
a=Aset()     
b=Aset()
a.add(1)  
a.add(2)
a.add(3)
b.add(4)
b.add(5)
b.add(6)
c=Aset.union(a, b)
c.display()

    