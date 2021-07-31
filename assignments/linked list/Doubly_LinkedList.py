class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList():
    def __init__(self):
        self.start=None

    def display(self):
        if self.start is None:
            print("List is empty")
        else:
            p=self.start
            while p is not None:
                print(p.value, end=' ')
                p= p.next

        return self.start

    def insert_in_empty_list(self,data):
        node = Node(data)
        self.start = node


    def insert_in_beginning(self, data):
        # if list is empty
        if self.start is None:
            self.insert_in_beginning(data)
        else:
            node= Node(data)
            node.next= self.start
            self.start.prev= node
            self.start = node
        return self.start

    def insert_at_end1(self, data):
        if self.start is None:
            self.insert_in_empty_list(data)
            return
        else:
            node=Node(data)
            p=self.start
            prevNode=p
            while p is not None:
                prevNode=p
                p=p.next
            node.prev =prevNode
            prevNode.next= node

    def insert_at_end2(self, data):
        if self.start is None:
            self.insert_in_empty_list(data)
            return
        else:
            node=Node(data)
            p=self.start
            while p.next is not None:
                p=p.next
            p.next = node
            node.prev= p

    def create(self):
        n= int(input(" Enter number of nodes : "))
        if n==0:
            return

        for i in range(n):
            data = int(input("Enter element to be inserted : "))
            self.insert_at_end1(data)
        return self.start

    def insert_after(self, data, llVal):
        node= Node(data)
        p= self.start
        while p is not None:
            if p.value== llVal:
                break
            p= p.next

        if p is None:
            print(f'{llVal} is not in the list')
            return

        else:
            node.next = p.next
            node.prev=p
            if p.next is not None:
                p.next.prev = node
            p.next = node
        return self.start

    def insert_before(self, data, llVal):
        node= Node(data)
        if self.start is None:
            print("list is empty")
            return

        if self.start.value == llVal:
            node.next = self.start
            self.start.prev= node
            self.start = node
            return self.start

        p=self.start
        while p is not None:
            if p.value == llVal:
                break
            p= p.next

        if p is None:
            print(llVal, " is not in the list")
            return
        else:
            node.prev = p.prev
            node.next = p
            p.prev.next = node
            p.prev=node

    def delete_first_node(self):
        pass
    def delete_last_node(self):
        pass
    def delete_node(self, llVal):
        pass
    









list = DoublyLinkedList()
list.create()

while True:
    print("")
    print("1. Display list")
    print("1. Insert in empty list")
    print("3. Insert a node in the beginning of the list")
    print("4. Insert a node at the end of the list")
    print("5. Insert a node after a specified node")
    print("6. Insert a node before a specified node")
    print("7. Delete first node")
    print("8. Delete last node")
    print("9. Delete any node")
    print("10. Reverse the list")
    print("11. Quit")


    option = int(input("Enter your choice: "))

    if option == 1:
        list.display()
    elif option == 2:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_empty_list(data)
    elif option == 3:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted : "))
        list.insert_at_end1(data)

    elif option == 11:
        break
    else:
        print("Wrong option")


