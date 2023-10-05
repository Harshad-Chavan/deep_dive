class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            print(current.value)
            current = current.next
        current.next = new_node


        return

    def __str__(self):
        current = self.head
        output = []
        if current:
            while current.next is not None:
                output.append(str(current.value))
                current = current.next
            output.append(str(current.value))
            return "->".join(output)
        else:
            return "Empty List"


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.insert(10)
    mylist.insert(2)
    mylist.insert(5)
    mylist.insert(8)
    print(mylist)