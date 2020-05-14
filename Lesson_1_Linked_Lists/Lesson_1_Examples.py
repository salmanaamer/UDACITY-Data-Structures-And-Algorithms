class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def create_linked_list(input_list):
    head = None
    current_node = head
    for x in input_list:
        if x == input_list[0]:
            head = Node(x)
            current_node = head # we are using pointers ??
        else: 
            current_node.next = Node(x)
            current_node = current_node.next
        print (current_node.value)
    return head

input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
