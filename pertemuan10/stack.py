"""
Stack dalam Python adalah struktur data linear yang mengikuti prinsip LIFO (Last In, First Out), 
di mana elemen terakhir yang dimasukkan adalah yang pertama kali dihapus. 
Analogi terbaiknya adalah tumpukan piring: 
Anda menambah atau mengambil piring hanya dari bagian paling atas. 
Operasi utamanya adalah push (menambah) dan pop (menghapus).
"""

stack = []
# Push (menambah data)
stack.append('A')
stack.append('B')
# Pop (menghapus data teratas)
top = stack.pop() # Mengeluarkan 'B'

#cara kedua, menggunakan collections.deque

from collections import deque
stack = deque()
stack.append('A')
stack.pop()

stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))