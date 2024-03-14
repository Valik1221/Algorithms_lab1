class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_to_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def remove_from_end(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node


    def remove_from_front(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def is_empty(self):
        return self.head is None

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


# Мішок
linked_list_bag = LinkedList()
linked_list_bag.add_to_end(1)
linked_list_bag.add_to_end(2)
linked_list_bag.add_to_end(3)
linked_list_bag.print_list()  

linked_list_bag.remove_from_end()
linked_list_bag.print_list()  

# Черга
linked_list_queue = LinkedList()
linked_list_queue.add_to_end(1)
linked_list_queue.add_to_end(2)
linked_list_queue.add_to_end(3)
linked_list_queue.print_list()  

linked_list_queue.remove_from_front()
linked_list_queue.print_list() 

# Стек
linked_list_stack = LinkedList()
linked_list_stack.add_to_front(1)
linked_list_stack.add_to_front(2)
linked_list_stack.add_to_front(3)
linked_list_stack.print_list()  

linked_list_stack.remove_from_front()
linked_list_stack.print_list() 
