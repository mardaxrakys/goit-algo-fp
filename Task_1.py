class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, list1, list2):
        dummy = Node(0)
        tail = dummy

        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next

    def insertion_sort(self):
        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def _sorted_insert(self, sorted_list, new_node):
        if not sorted_list or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            return new_node
        else:
            current = sorted_list
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return sorted_list

# Приклад використання

# Створення першого списку та його реверсування
llist1 = LinkedList()
llist1.append(10)
llist1.append(30)
llist1.append(20)
llist1.append(5)

print("Початковий список 1:")
llist1.print_list()

llist1.reverse()
print("Реверсований список 1:")
llist1.print_list()

# Створення другого списку та сортування
llist2 = LinkedList()
llist2.append(15)
llist2.append(35)
llist2.append(25)
llist2.append(5)

print("Початковий список 2:")
llist2.print_list()

llist2.insertion_sort()
print("Відсортований список 2:")
llist2.print_list()

# Об'єднання двох відсортованих списків
merged_list = LinkedList()
merged_list.head = llist1.sorted_merge(llist1.head, llist2.head)

print("Об'єднаний відсортований список:")
merged_list.print_list()
