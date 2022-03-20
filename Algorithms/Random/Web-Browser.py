# Web Browser Implementation using Linked List in Python

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self, homepage):
        node = Node(homepage)
        self.head = node
        self.tail = node
        self.current = node
        self.size = 1
    
    def visit(self, value):
        node = Node(value)

        if self.current.next:
            self.current.next = None
            node.prev = self.current
            self.current.next = node
            self.current = self.current.next    
            if self.current.prev:
                self.tail.prev = self.current.prev
                self.tail.next = None
                self.tail = self.current

        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
            self.current = self.current.next
    
    def back(self, n) -> str:
        if n > 0:
            i = 0
            while i != n:
                if self.current == self.head:
                    break
                self.current = self.current.prev
                i+=1
            
            return self.current.value
    
    def forward(self, n) -> str:
        if n > 0:
            i = 0
            while i != n:
                if self.current == self.tail:
                    break
                self.current = self.current.next
                i+=1
            
            return self.current.value


class WebBrowser:
    def __init__(self, homepage):
        self.browser = LinkedList(homepage)

    def visit(self, page):
        self.browser.visit(page)
        

    def back(self, n):
        current = self.browser.back(n)
        return current

    def forward(self, n):
        current = self.browser.forward(n)
        return current
