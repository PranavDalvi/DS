class Lnode:
    def __init__(self,data):
        self.data = data
        self.next = None

def prepend(head, val):
    newNode = Lnode(val) # class Lnode is defined already
    newNode.next = head
    head = newNode
    return head

def traverseandPrint(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode= curNode.next

def delete(head, x):
    predNode = None
    curNode = head
    while curNode is not None and curNode.data is not x:
        predNode = curNode
        curNode = curNode.next
    if curNode == head:
        head = curNode.next
    else:
        predNode.next = curNode.next

#Driver code
head = Lnode(100)       # List created
head = prepend(head,50) # Insert as many elements as wanted
traverseandPrint(head)  # Every operation followed by print
delete(head, 50)
traverseandPrint(head)

# output
# 50
# 100
# 50 
# 100
