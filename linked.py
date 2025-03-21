class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


    def __iter__(self):
        lst = []
        ptr = self
        while ptr:
            lst.append(ptr.data)
            ptr = ptr.next
        return iter(lst)

    def __str__(self):
        return '<' + ', '.join([str(x) for x in self]) + ">"

    def to_list(self):
        return [x for x in self]

    def __repr__(self):
        return ' --> '.join([str(x) for x in self])

    @staticmethod
    def delete(n, ptr):
        if ptr is None:
            return None
        if ptr.data is n:
            return ptr.next
        else:
            return Node(ptr.data, Node.delete(n, ptr.next))

    def add_tail(self, data):
        ptr = self
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(data, None)
        return self

    @staticmethod
    def insert(data , ptr):
        if ptr is None:
            return Node(data, None)
        elif ptr.data > data:
            return Node(data, ptr)
        else:
            return Node(ptr.data, Node.insert(data, ptr.next))

    @staticmethod
    def sort(ptr):
        if ptr is None:
            return ptr
        elif ptr.next is None:
            return ptr
        else:
            return Node.insert(ptr.data, Node.sort(ptr.next))

    def reverse(self):
        if self is None:
            return None
        elif self.next is None:
            return Node(self.data, None)
        else:
            return self.next.reverse().add_tail(self.data)

    def __len__(self):
        if self is None:
            return 0
        if self.next is None:
            return 1
        return 1 + self.next.__len__()

def main():

    l1 = None
    for n in [6, 10, 2, 4, 8, 12]:
        l1 = Node(n, l1)

    print(l1.data)
    print(l1.__repr__())
    l1.add_tail(16)
    print(l1)
    l1 = Node(19, l1)
    print(l1)
    print(l1.__repr__())

    print('\n', '-+-'* 20, '\n')
    l2 = None
    for x in [6, 10, 2, 4, 8, 12]:
        l2 = Node.insert(x, l2)

    print(f'l2 = {l2}')
    #print(Node.sort(l1).__repr__())
    l1 = Node.delete(18, l1)
    print(l1)
    print('\n', '-+-' * 20, '\n')
    print(l1)
    print(l1.to_list())
    print('-='*20)
    print(f'l2 = {l2}')
    print(f'reverse of l2 = {l2.reverse()}')
    print(f'l2 = {l2}')
    print(l2.__len__())
    print(len(l2))

if __name__ == "__main__":
    main()


