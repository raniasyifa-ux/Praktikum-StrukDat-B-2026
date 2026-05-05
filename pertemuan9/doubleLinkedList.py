class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# ================= INSERT =================

def insert_awal(head, data):
    new_node = Node(data)
    new_node.next = head

    if head:
        head.prev = new_node

    return new_node


def insert_akhir(head, data):
    new_node = Node(data)

    if not head:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next

    temp.next = new_node
    new_node.prev = temp

    return head


def insert_tengah(head, key, data):
    temp = head

    while temp:
        if temp.data == key:
            new_node = Node(data)

            new_node.next = temp.next
            new_node.prev = temp

            if temp.next:
                temp.next.prev = new_node

            temp.next = new_node
            break

        temp = temp.next

    return head


# ================= HAPUS =================

def hapus(head, key):
    temp = head

    while temp:
        if temp.data == key:

            if temp.prev:
                temp.prev.next = temp.next
            else:
                head = temp.next

            if temp.next:
                temp.next.prev = temp.prev

            break

        temp = temp.next

    return head


# ================= TAMPIL =================

def tampil_maju(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


def tampil_mundur(head):
    if not head:
        return

    temp = head
    while temp.next:
        temp = temp.next

    while temp:
        print(temp.data, end=" ")
        temp = temp.prev
    print()


# ================= MAIN =================

head = None

head = insert_awal(head, 10)
head = insert_akhir(head, 20)
head = insert_akhir(head, 30)
head = insert_tengah(head, 20, 25)

print("Maju:")
tampil_maju(head)

print("Mundur:")
tampil_mundur(head)

head = hapus(head, 20)

print("Setelah hapus:")
tampil_maju(head)



