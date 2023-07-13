class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def float(self, k):
        while k // 2 > 0:
            if self.heap[k].freq < self.heap[k//2].freq:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.float(self.size)

    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.minchild(k)
            if self.heap[k].freq > self.heap[mc].freq:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def minchild(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k*2].freq < self.heap[k*2+1].freq:
            return k * 2
        else:
            return k * 2 + 1

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

    def printQueue(self):
        print("[", end = "")
        for i in range(1, len(self.heap)):
            print(self.heap[i].freq, end = ", ")
        print("]")
        for i in range(1, len(self.heap)):
            print(self.heap[i].left, end = ", ")
        print()
        for i in range(1, len(self.heap)):
            print(self.heap[i].right, end = ", ")
        print()
    
class QueueNode:

    def __init__(self, data = None, freq = None, left = None, right = None):
        self.data = data
        self.freq = freq
        self.left = left
        self.right = right

    def isLeaf(self):
        return (self.left == None and self.right == None)

codes = {"A":5, "B":12, "C":35, "D":3, "E":8, "F":14, "G":21, "H":1, "I":39}

def Huffman(dict):
    # Number of characters to encode.
    heap_len = len(dict)
    # Initialize Queue
    h = Heap()
    for key, value in dict.items():
        h.insert( QueueNode(key, value) )
    #h.printQueue()
    # Extract the two nodes of lower frequency and merge them in Q
    for n in range(heap_len - 1):
        #print("Iteration: ", n)
        z = QueueNode("$")
        z.left = h.pop()
        z.right = h.pop()
        z.freq = z.left.freq + z.right.freq
        #print(z.freq)
        h.insert(z)
        #h.printQueue()
    return h.pop()

# print(Huffman(codes).right)

def printCode(Hroot, code):
    #print("root freq: ", Hroot.freq)
    #print("root left: ", Hroot.left)
    if Hroot.left != None:
        code.append(0)
        printCode(Hroot.left, code)
        #print(code)
        code.pop(-1)

    if Hroot.right != None:
        #print(Hroot.right.freq)
        code.append(1)
        printCode(Hroot.right, code)
        code.pop(-1)

    if Hroot.isLeaf():
        print(f"{Hroot.data}: ", end = "")
        for i in code:
            print(i, end = "")
        print()

root = Huffman(codes)

code = []
printCode(root, code)

