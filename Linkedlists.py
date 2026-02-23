# Nodes 

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.text = None

# class linkedList:
#     def __init__(self):
#         self.head = None

#     def insertAtFirst(self,data):
#         newNode = node(data)
#         newNode.address = self.head
#         self.head = newNode

class Node:
    def __init__(self,myData):
        self.data = myData
        self.address = None

class linkedList:
    def __init__(self):
        self.head = None

    def insertAtFirst(self,myData):
        newNode = Node(myData)
        newNode.address = self.head
        self.head = newNode

    def traversal(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.address

MyLinkedList = linkedList()
MyLinkedList.insertAtFirst(10)
MyLinkedList.insertAtFirst(20)
MyLinkedList.insertAtFirst(30)

MyLinkedList.traversal()