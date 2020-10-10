class Node():
    def __init__ (self,elem):
        self.elem = elem
        self.next = None
class SingleLinkList(object):
    def __init__ (self,node=None):
        self.head = node
    def is_empty(self):
        return self.head ==None
    def length(self):
        sum = 0
        cur = self.head
        while cur != None:
            sum+=1
            cur = cur.next
        return sum
    def travel(self):
        cur = self.head
        while cur!=None:
            print(cur.elem,end = '-->')
            cur = cur.next
    def append(self,item):
        node = Node(item)
        cur = self.head
        if self.is_empty():
            self.head = node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    def add(self,item):
        node=Node(item)
        node.next = self.head
        self.head = node
    def insert(self,index,item):
        if index<=0:
            self.add(item)
        elif index>(self.length() -1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            node.next = cur.next
            cur.next=node
    def remove(self,item):

        pre = None
        cur = self.head
        while cur != None:

            if cur.elem == item:
                # Is this a head node?
                if cur == self.head:
                    self.head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next
    def search(self,item):
        cur = self.head
        while cur!= None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False







if __name__ == "__main__":
    ll = SingleLinkList()
    # print(ll.is_empty())
    # print(ll.length())
    ll.append(1)
    ll.append(2)
    ll.append(1)
    ll.append(2)
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.remove(2)
    ll.travel()


