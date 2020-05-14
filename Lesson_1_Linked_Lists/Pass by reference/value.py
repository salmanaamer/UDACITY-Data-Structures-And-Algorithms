class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def create_linked_list():
    head = Node(17)
    #x = head.value
    current_node = head
    head.next = Node(23)
    print("head value and current value ", hex(id(head)), hex(id(current_node)))
   # print(id(head.value))
   # print(id(x))
    head.value = 19
    print("after val change", hex(id(head)), hex(id(current_node)))
  #  print(id(head.value))
  #  print(id(x))
  #  print(" final head address and curr", head.value, x)


  
# pass by value 
def f1(a):
    a = a+5
#a = 10
#f1(a)
#print(a)

# pass by reference
def f2(a):
    a.value = 7
a = Node(10)
f2(a)
print(a.value)
