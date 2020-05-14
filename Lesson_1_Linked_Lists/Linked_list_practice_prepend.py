class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
# initialisation
    def __init__(self):
        self.head = None
# append function   
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return
# to list function
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

# Define a function outside of the class

#prepend
def prepend(self, value):
    new_node = Node(value)
    new_node.next = self.head # both nodes point to same object
    self.head = new_node
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    pass


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend  # why does this work ???

#search linked list for node 
def search(self, value):
    node = self.head
    while node:
        if (node.value == value):
            print ("in list")
            return 
        else:
            node = node.next
    pass
    """ Search the linked list for a node with the requested value and return the node. """
LinkedList.search = search

## what to return for this function ?
def remove(self, value):
    """ Remove first occurrence of value. """
    curr_node = self.head
    prev_node = None
    while curr_node:
        if (curr_node.value == value):
            #First Element is the value to remove
            if (self.head.value == value):
                self.head = self.head.next
                return
            # all other elements
            else:
                prev_node.next = curr_node.next # this will change head.next as head.next is part of the object node
                return 

        else:
            prev_node = curr_node
            curr_node = curr_node.next
    pass

    pass

LinkedList.remove = remove



p1 = LinkedList()
p1.append(3)
p1.append(42)
p1.prepend(1)


def print_linked_list(mylist):
    node = mylist.head
    while node:
        print(node.value)
        node = node.next

print_linked_list (p1)

p1.remove (42)
print("after remove")
print_linked_list (p1)