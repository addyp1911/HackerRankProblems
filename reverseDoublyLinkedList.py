class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def print_list(self, head):
        temp = head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print("\n")

    def reverse(self, head):
        temp = head
        prev_node = None
        while temp:
            current = temp
            temp = temp.next
            current.next = prev_node
            if prev_node:
                prev_node.prev = current
            prev_node = current
        return prev_node

if __name__ == "__main__":
    obj =  DoublyLinkedList()
    size = int(input("enter the size of the linked list = "))
    for ele in range(size):
        data = input("enter the element for the linked list = ")
        obj.add_first(data)
    obj.print_list(obj.head)
    print("head of the linked list = ", obj.head.data) 
    head = obj.reverse(obj.head)
    obj.print_list(head)

