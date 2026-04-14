class Node:
    """
    Node class for Doubly Linked List
    Each node has: data, pointer to next node, pointer to previous node
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to next node
        self.prev = None  # Points to previous node


class DoublyLinkedList:
    """ 
    Doubly Linked List Implementation
    Features: Insert at beginning/end, delete, traverse forward/backward, search
    """
    
    def __init__(self):
        self.head = None  # First node
        self.tail = None  # Last node
    
    def is_empty(self):
        """Check if list is empty"""
        return self.head is None
    
    def insert_at_beginning(self, data):
        """Insert a new node at the beginning"""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_at_end(self, data):
        """Insert a new node at the end"""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def insert_at_position(self, data, position):
        """Insert a new node at specified position (0-indexed)"""
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        count = 0
        
        while current and count < position - 1:
            current = current.next
            count += 1
        
        if current is None:
            print("Position out of bounds")
            return
        
        if current.next is None:
            self.insert_at_end(data)
        else:
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
    
    def delete_at_beginning(self):
        """Delete the first node"""
        if self.is_empty():
            print("List is empty")
            return
        
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
    
    def delete_at_end(self):
        """Delete the last node"""
        if self.is_empty():
            print("List is empty")
            return
        
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    
    def delete_by_value(self, value):
        """Delete first node with given value"""
        if self.is_empty():
            print("List is empty")
            return
        
        current = self.head
        
        while current:
            if current.data == value:
                if current == self.head:
                    self.delete_at_beginning()
                elif current == self.tail:
                    self.delete_at_end()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
        
        print(f"Value {value} not found")
    
    def search(self, value):
        """Search for a value in the list"""
        current = self.head
        position = 0
        
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return -1  # Not found
    
    def display_forward(self):
        """Display list from head to tail"""
        if self.is_empty():
            print("List is empty")
            return
        
        current = self.head
        print("Forward: ", end="")
        while current:
            print(f"{current.data}", end=" <-> " if current.next else "\n")
            current = current.next
    
    def display_backward(self):
        """Display list from tail to head"""
        if self.is_empty():
            print("List is empty")
            return
        
        current = self.tail
        print("Backward: ", end="")
        while current:
            print(f"{current.data}", end=" <-> " if current.prev else "\n")
            current = current.prev
    
    def get_length(self):
        """Get the number of nodes in the list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def reverse(self):
        """Reverse the doubly linked list"""
        if self.is_empty() or self.head == self.tail:
            return
        
        current = self.head
        self.head, self.tail = self.tail, self.head
        
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev  # Move to next (which is now prev)


# Example usage and demonstrations
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    print("=== Doubly Linked List Demo ===\n")
    
    # Insert elements
    print("1. Inserting elements at end: 10, 20, 30")
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.display_forward()
    dll.display_backward()
    
    # Insert at beginning
    print("\n2. Inserting 5 at beginning")
    dll.insert_at_beginning(5)
    dll.display_forward()
    
    # Insert at position
    print("\n3. Inserting 15 at position 2")
    dll.insert_at_position(15, 2)
    dll.display_forward()
    
    # Length
    print(f"\n4. Length of list: {dll.get_length()}")
    
    # Search
    print("\n5. Searching for value 20")
    pos = dll.search(20)
    if pos != -1:
        print(f"Found at position: {pos}")
    else:
        print("Not found")
    
    # Delete operations
    print("\n6. Deleting from beginning")
    dll.delete_at_beginning()
    dll.display_forward()
    
    print("\n7. Deleting from end")
    dll.delete_at_end()
    dll.display_forward()
    
    print("\n8. Deleting value 15")
    dll.delete_by_value(15)
    dll.display_forward()
    
    # Reverse
    print("\n9. Reversing the list")
    dll.reverse()
    dll.display_forward()
    dll.display_backward()
