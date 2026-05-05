class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ================= INSERT =================

def insert_awal(head, data):
    new_node = Node(data)

    if head is None:
        new_node.next = new_node
        return new_node

    temp = head
    while temp.next != head:
        temp = temp.next

    temp.next = new_node
    new_node.next = head
    head = new_node

    return head


def insert_akhir(head, data):
    new_node = Node(data)

    if head is None:
        new_node.next = new_node
        return new_node

    temp = head
    while temp.next != head:
        temp = temp.next

    temp.next = new_node
    new_node.next = head

    return head


def insert_tengah(head, key, data):
    if head is None:
        return None

    temp = head
    while True:
        if temp.data == key:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
            break

        temp = temp.next
        if temp == head:
            break

    return head


# ================= HAPUS =================

def hapus(head, key):
    if head is None:
        return None

    # hanya 1 node
    if head.next == head and head.data == key:
        return None

    # hapus head
    if head.data == key:
        last = head
        while last.next != head:
            last = last.next

        head = head.next
        last.next = head
        return head

    # hapus selain head
    temp = head
    while temp.next != head:
        if temp.next.data == key:
            temp.next = temp.next.next
            break
        temp = temp.next

    return head


# ================= TAMPIL =================

def tampil(head):
    if head is None:
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()


# ================= MAIN =================

head = None

head = insert_awal(head, 10)
head = insert_akhir(head, 20)
head = insert_akhir(head, 30)
head = insert_tengah(head, 20, 25)

print("Data:")
tampil(head)

head = hapus(head, 20)

print("Setelah hapus:")
tampil(head)