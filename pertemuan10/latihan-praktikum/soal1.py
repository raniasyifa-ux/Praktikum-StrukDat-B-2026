class StackList:
    def __init__(self):
        self.items = []

    def is_empty(self):
         return len(self.items) == 0
    
    def push(self, url):
         self.items.append(url)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.items.pop()
        
    def peek(self):
        if self.isEmpty():
            return "stack nya kosong"
        else:
            return self.items.pop()
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    

punyaku = StackList()

punyaku.push("AYAH")
punyaku.push ("IBU")
punyaku.push ("ADEK")
punyaku.push ("KAKAK")

print("Stacknya : ", punyaku.items)

print("pop: ", punyaku.pop())

print(" stack setelah di pop: ", punyaku.items)

print('peek: ', punyaku.peek())

print("isEmptynya: ", punyaku.is_empty())

print("sizenya: ", punyaku.size())


