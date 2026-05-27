class Node:
    def __init__(self, data = None):
      self.data = data; 
      self.next = None;

class LinkedList:
    def __init__(self, head = None):
      self.head = head;
    
    def get(self, index: int) -> int:
        if (self.head == None):
            return -1
        current = self.head

        for i in range(index):
          if current.next:
            current = current.next 
          else:
            return -1
        return current.data

    def insertHead(self, val: int) -> None:
      new_node = Node(val)
      if (self.head == None):
          self.head = new_node
          return
      new_node.next = self.head
      self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if (self.head == None):
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next
        
        current.next = new_node

    def remove(self, index: int) -> bool:
        print(self.printLL())
        if (self.head is None):
            return False

        current = self.head

        if ( index == 0 ):
            self.head = self.head.next
            return True
                
        for i in range(index):
            if current.next:
                if (i == (index - 1)):
                    # print(i, current.data)
                    if (current.next.next is not None):
                        current.next = current.next.next
                        return True
                    else: 
                        current.next = None
                        return True
                current = current.next
            else: return False
        return False

    def getValues(self) -> List[int]:
      self.printLL()
      arr = []

      if (self.head == None):
          return []

      current = self.head

      while current is not None:
          arr.append(current.data)
          current = current.next
      
      return arr

    def printLL(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next 