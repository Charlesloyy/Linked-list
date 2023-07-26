import random as rd

class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None
        
class ListLinked:
    def __init__(self):
        self.head = Node()
        
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur=cur.next
        cur.next = new_node
        
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
        
    def get_element(self, index):
        if index >= self.length():
            print("INDEX ERROR: Out of index range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data 
            cur_idx +=1
            
    def delete(self, index):
        if index >= self.length():
            print("INDEX ERROR: Out of index range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx +=1


mylist = ListLinked()
for _ in range(20):
    mylist.append(rd.randint(0,20))
    
mylist.display()
mylist.delete(4)
mylist.delete(10)  
print(mylist.get_element(0))
mylist.display()
print(mylist.length())