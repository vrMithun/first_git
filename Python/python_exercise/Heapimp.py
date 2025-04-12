class Heap:
    def __init__(self):
        self.heap = [None]  # Dummy element at index 0 for 1-based indexing

    def add(self, tuple_):
        self.heap.append(tuple_)
        self.upheap(len(self.heap) - 1)

    def upheap(self, index):
        parent = index // 2
        while parent > 0 and self.heap[index][0] > self.heap[parent][0]:  # Max-heap condition
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = index // 2

    def extract_max(self):
        if len(self.heap) <= 1:  # Heap is empty
            return None
        max_val = self.heap[1]
        last = self.heap.pop()  # Remove the last element
        if len(self.heap) > 1:
            self.heap[1] = last
            self.downheap(1)
        return max_val

    def downheap(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index

        # Max-heap condition: Compare with left child
        if left < len(self.heap) and self.heap[largest][0] < self.heap[left][0]:
            largest = left

        # Max-heap condition: Compare with right child
        if right < len(self.heap) and self.heap[largest][0] < self.heap[right][0]:
            largest = right

        # Swap and continue downheaping if needed
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.downheap(largest)

    def getHeap(self):
        print(self.heap[1:])  # Exclude the dummy element

    def kth(self, num):
        temp_heap = self.heap # Create a copy of the heap
        for _ in range(num - 1):
            self.extract_max()
        result = self.extract_max()
        self.heap = temp_heap  # Restore the heap
        print(result)


# Example usage
myobj = Heap()
myobj.add((8, 'a'))
myobj.add((2, 'b'))
myobj.add((7, 'c'))
myobj.add((4, 'g'))
myobj.getHeap() 
print(myobj.extract_max())
myobj.getHeap()  # Heap remains intact
