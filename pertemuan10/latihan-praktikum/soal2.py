class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        if self.top is None:
         return self.count == 0
        else: 
            return "List ada Isi"


    def push(self, url):
        nodeBaru = Node(url)
        if self.top == None:
            self.top = nodeBaru
        else:
            nodeBaru.next = self.top
            self.top = nodeBaru
        self.count += 1



    def pop(self):
        if self.is_empty():
            return "KOSONGG"
        else:
            yangdihapus = self.top
            self.top = self.top.next
        
        self.count -= 1
        return yangdihapus.url

    def peek(self):
        if self.is_empty():
            return "STACK KOSONG"
        return self.top.url
    

    def size(self):
        return self.count
    
    def tampil(self):
        current = self.top
        while current:
            print(current.url, end=" -> ")
            current = current.next
        print("None")

URL = StackLinkedList()

URL.push("WEBTOON")
URL.push('MANGATOON')
URL.push("BSTASTION")

print("STACK: ", URL.tampil())

print("pop: ", URL.pop())

print("STACK SETELAH DI POP: ", URL.tampil())
print("peek: ", URL.peek())
print("size: ", URL.size())
