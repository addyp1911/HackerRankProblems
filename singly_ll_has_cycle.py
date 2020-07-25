class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        return self.head 

    def print_ll(self,head):
        temp = head
        while temp:
            print(temp.data, end=",")  
            temp = temp.next
        print()

    def has_cycle(self, head):
        slow_ptr = fast_ptr = head
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
            else:
                return False

if __name__== "__main__":
    ll = SinglyLinkedList()
    ll.insert(10)
    ll.insert(19)
    ll.insert(23)
    ll.print_ll(ll.head)
    x = ll.has_cycle(ll.head)    
    print(x)            