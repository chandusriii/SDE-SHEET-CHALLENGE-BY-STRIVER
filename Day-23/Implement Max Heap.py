class Solution:

    def initializeHeap(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1

        # Bubble Up
        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] < self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break

    def getMax(self):
        return self.heap[0] if self.heap else -1

    def extractMax(self):
        if not self.heap:
            return

        n = len(self.heap)

        if n == 1:
            self.heap.pop()
            return

        self.heap[0] = self.heap[-1]
        self.heap.pop()

        self.heapify(0)

    def heapSize(self):
        return len(self.heap)

    def isEmpty(self):
        return 1 if len(self.heap) == 0 else 0

    def changeKey(self, ind, val):
        old_val = self.heap[ind]
        self.heap[ind] = val

        # If value increased, bubble up
        if val > old_val:
            i = ind

            while i > 0:
                parent = (i - 1) // 2

                if self.heap[parent] < self.heap[i]:
                    self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                    i = parent
                else:
                    break

        # If value decreased, heapify down
        else:
            self.heapify(ind)

    def heapify(self, i):
        n = len(self.heap)

        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            # If left and right are equal, LEFT child is preferred
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest
