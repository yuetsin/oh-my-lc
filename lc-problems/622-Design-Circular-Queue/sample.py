#!/usr/bin/env python


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.filled = 0
        self.q = [0]*self.size
        self.head = self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            # no elements yet
            if self.head is None and self.tail is None:
                self.head = self.tail = 0

            else:  # some elements
                self.tail = (self.tail+1) % self.size
            self.q[self.tail] = value
            self.filled += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = (self.head+1) % self.size
        self.filled -= 1
        return True

    def Front(self) -> int:
        return self.q[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.q[self.tail] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.filled == 0

    def isFull(self) -> bool:
        return self.filled == self.size
