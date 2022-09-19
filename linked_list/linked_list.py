#Building the Node class
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

#Building the Linked List class
class LinkedList:
    def __init__(self):
        self.head=None

    def traverse_my_list(self):
        temp=self.head
        while temp is not None:
            print (temp.data)
            temp= temp.next

#Insert new node to the end (tail) of the linked list
    def insert_to_tail(self, data):
        current= self.head
        if self.head== None:
            return Node(data)
        while current.next != None:
            current= current.next
        current.next= Node(data)
        return self.head

week_days= LinkedList()

week_days.head= Node("Mon")
node1= Node("Tue")
node2= Node("wed")
node3= Node("Thu")
week_days.insert_to_tail("Thu")

#not finished. supposed to be sent on discord