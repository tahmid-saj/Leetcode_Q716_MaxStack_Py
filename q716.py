from heapq import *
class MaxStack:

    def __init__(self):
        self.maxHeap = []
        self.stk = []
        self.deleted = set()
        self.i = 0

    def push(self, x: int) -> None:
        self.stk.append((x, self.i))
        heappush(self.maxHeap, (-x, -self.i))
        self.i += 1

    def pop(self) -> int:
        while self.stk and self.stk[-1][1] in self.deleted: self.stk.pop()

        res = self.stk.pop()
        if -self.maxHeap[0][1] == res[1]: heappop(self.maxHeap)
        else: self.deleted.add(res[1])
        return res[0]

    def top(self) -> int:
        while self.stk and self.stk[-1][1] in self.deleted: self.stk.pop()
        return self.stk[-1][0]

    def peekMax(self) -> int:
        while self.maxHeap and -self.maxHeap[0][1] in self.deleted: heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    def popMax(self) -> int:
        while self.maxHeap and -self.maxHeap[0][1] in self.deleted: heappop(self.maxHeap)
        
        res = heappop(self.maxHeap)
        if -res[1] == self.stk[-1][1]: self.stk.pop()
        else: self.deleted.add(-res[1])
        return -res[0]


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
