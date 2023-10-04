class node:
    def __init__(self,val):
        self.data=val
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def create(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def add_middle(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            fp=self.head
            sp=self.head
            t=self.head
            while fp!=None and fp.next!=None:
                fp=fp.next.next
                sp=sp.next
            while t.next != sp:
                t=t.next
            temp=node(x)
            t.next=temp
            temp.next=sp
    def add_at_specified(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            pos=int(input("enter the pos of the node to be added"))
            t=self.head
            count=1
            while(count<pos-1):
                t=t.next
                count+=1
            temp=node(x)
            temp.next=t.next
            t.next=temp
    
    def display(self):
        if self.head==None:
            print("node is not present")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end="->")
                temp=temp.next
a=linkedList()
a.create(10)
a.create(20)
a.create(30)
a.create(40)
a.add_at_specified(99)
a.display()
