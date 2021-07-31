class Node:
    def __init__(self, value):
        self.value = value
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None

    def  display_list(self):
        if self.start is None:
            print(" the linked list is empty")
        else:
            print("the linked list is: ")
            p=self.start
            while p is not None:
                print(p.value, end=" ")
                p = p.link

    def count_list(self):
        n=0
        p=self.start
        while p is not None:
            n+=1
            p=p.link
        print("******************** total number of nodes are:", n)
        return n

    def search(self, x): # search is value x exist in the linked list
        position =1
        p=self.start
        while p is not None:
            if p.value == x:
                print(f'******************** {x} is at position {position}')
                break
            position+=1
            p = p.link

        else:
            print(x, "******************** is not in the list ")

    def insert_in_beginning(self, value):
        node = Node(value)
        node.next = self.start
        self.start= node

    def insert_at_end(self, inputVal):
        node= Node(inputVal)
        # print(node.value)
        if self.start is None:
            self.start = node
            return self.start
        p=self.start
        while p.link is not None:
            p=p.link
        p.link = node
        return self.start

    def create(self):
        n = int(input("number of nodes : "))
        while n>0:
            node = (int(input("enter node value: ")))
            self.insert_at_end(node)
            n-=1
    def insert_after_specific_node(self, data, x):
        p= self.start
        while p is not None:
            if p.value == x:
                break
            p=p.link
        # p=p.link
        if p is None:
            print(f"******************** item {x} wa not found")
            return
        else:
            node = Node(data)
            node.link = p.link
            p.link = node
            return

    def insert_before_specific_node(self, data, x):
        #If list is  empty
        if self.start is None:
            print("******************* list is empty")

        if self.start.value == x:
            node = Node(x)
            node.link = self.start.link
            self.start = node
            return

        #If list is not empty
        p=self.start
        while p.link is not None:
            if p.link.value == x:
                break
            p= p.link

        if p.link is None:
            print(f'******************** item {x} was not found in the list')
        else:
            node = Node(data)
            node.link = p.link
            p.link = node

    def insert_at_position(self, data, x):
        position =1

        if x==1:
            node = Node(data)
            node.link = self.start
            self.start = node
            return self.start
        p=self.start
        while position<x and p is not None:
            p= p.link
            position+=1
        if p is None:
            print(f'******************** position {x} out of range')
        else:
            node = Node(data)
            node.link = p.link
            p.link = node
            return self.start

    def delete_node(self, x):
        #empty list
        if self.start is None:
            print("******************** list is empty")
        #first node
        elif self.start.value == x:
            self.start= self.start.link
            return self.start
        else:
            p=self.start
            while p.link is not None:
                if p.link.value == x:
                    p.link = p.link.link
                    break
                p= p.link

            return self.start

    def reverse_list(self):
        pass

    def bubble_sort_exdata(self):
        end = None

        while self.start.link != end:
            p=self.start
            while p.link != end:
                q= p.link
                if p.value >q.value:
                    p.value, q.value = q.value, p.value
                p=p.link
            end=p
        return self.start

    def bubble_sort_exlink(self):






list = SingleLinkedList()
list.create()

while True:
    print("\n")
    print("1. Display list")
    print("2. Count the number of nodes")
    print("3. Search for an element")
    print("4. Insert in empty list/Insert in the beginning of the list")
    print("5. Insert a node at the end of the list")
    print("6. Insert a node after a specified node")
    print("7. Insert a node before a specified node")
    print("8. Insert a node at a given position")
    print("9. Delete a node")
    print("10. Reverse the list")
    print("11. Bubble sort by exchanging data")
    print("12. Bubble sort by exchanging links")
    print("13. MergeSort")
    print("14. Insert Cycle")
    print("15. Detect Cycle")
    print("16. Remove Cycle")
    print("17. Quit")
    print("")

    option = int(input("Enter your choice : "))
    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_list()
    elif option == 3:
        data = int(input("Eneter the element to be searched : "))
        list.search(data)
    elif option ==4:
        data = int(input("Enter element to be added in the beginning of the list: "))
        list.insert_in_beginning(data)
    elif option==5:
        data = int(input("Enter element to be added at the end of the list: "))
        list.insert_at_end(data)
    elif option ==6:
        data = int(input("Enter element to be added at specific node: "))
        nodeMark = int(input("Enter mark node "))
        list.insert_after_specific_node(data, nodeMark)
    elif option == 7:
        data = int(input("Enter element to be added before specific node: "))
        nodeMark = int(input("Enter mark node "))
        list.insert_before_specific_node(data, nodeMark)
    elif option == 8:
        data = int(input("Enter element to be added at specific position: "))
        position = int(input("Enter position "))
        list.insert_at_position(data, position)
    elif option == 9:
        data = int(input("Enter element to be deleted: "))
        list.delete_node(data)



# 6. Insert a node after a specified node
# 7. Insert a node before a specified node
# 8. Insert a node at a given position
# 9. Delete first node
# 10. Delete last node
# 11. Delete any node

