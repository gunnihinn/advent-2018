class Double():

    def __init__(self, value=None):
        self.next = None
        self.prev = None
        self.value = value

    @staticmethod
    def from_list(items):
        if not items:
            return Double()

        head = Double(items[0])
        first = head

        for i in items[1:]:
            n = Double(i)
            n.prev = head
            head.next = n
            head = n

        return first

    def delete(self):
        if self.prev is None and self.next is None:
            return Double()

        if self.prev is None:
            self.next.prev = None
            return self.next

        if self.next is None:
            self.prev.next = None
            return self.prev

        (p, n) = (self.prev, self.next)
        p.next = n
        n.prev = p
        return n
