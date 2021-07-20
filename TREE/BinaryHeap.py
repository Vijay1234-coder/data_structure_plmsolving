
'''...............MIN HEAP....................'''

class BinHeap:
    def __init__(self):
        self.heapList  = [0]  # here our heap elements starts from index 1 always so 0th element we put 0
        self.currentSize = 0
    # Method of insertion;
    def perUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp=self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i]=temp
            i=i // 2
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.perUp(self.currentSize)

    def percDown(self,i):
        while(i*2) <= self.currentSize:
            mc = self.minChild

    '''its in complete'''








