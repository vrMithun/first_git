class listEmptyError(Exception):
	pass
class node:
	def _init_(self,data=None):
		self.data=data
		self.next=None


class sll:
	def _init_(self):
		self.head=None

	def insert_begin(self,data):
		new_node=node(data)
		new_node.next=self.head
		self.head=new_node

	def insert_end(self,data):
		new_node=node(data)
		if self.head is None:
			self.head=new_node
		current=self.head
		while current.next :
			current=current.next
		current.next=new_node

	def del_begin(self):
		if self.head is None:
			raise listEmptyError("list is empty")
		else:
			removed_element=self.head
			self.head=self.head.next
			return removed_element.data
			del(removed_element.data)

	def del_end(self):
		if self.head is None:
			raise listEmptyError("list is empty")
		elif self.head.next is None:
			removed_element=self.head
			self.head=None
			return removed_element
			del(removed_element.data)
		current=self.head
		while current.next is not None:
			current=current.next	
		removed_element=self.head
		self.head=None
		return removed_element.data
		del(removed_element)

	def insert_pos(self,data,pos):
		new_node=node(data)
		if pos==0:
			self.insert_begin(data)
			return
		current=self.head
		for i in range(pos-1):
			if current is None:
				raise listEmptyError("No element is found")
				return
			current=current.next
		new_node.next=current.next
		current.next=new_node

	def del_pos(self,pos):
		if self.head is None:
			raise listEmptyError("list is empty")
			return
		if pos==1:
			return self.del_begin()
		current=self.head
		for i in range(pos-1):
			if current is None or current.next is None:
				raise listEmptyError("element not in list")
			current=current.next
		removed_element=current.next
		if removed_element is None:
			raise listEmptyError("element not found")
		current.next=removed_element.next
		return removed_element.data

	def traversal(self):
		element=[]
		current=self.head
		while current is not None:
			element.append(current)
			current=current.next
		return element
		
			

		


if __name__ == '_main_':
    with open("sll1_in.txt", "r") as f:
        lines = f.readlines()
        
    sll = sll()  # Create an instance of SLL
    
    for r in lines:
        s = r.split()
        command = s[0]
        
        if command == "AB":  # Add at the beginning
            sll.add_begin(int(s[1]))
        elif command == "AE":  # Add at the end
            sll.add_end(int(s[1]))
        elif command == "DB":  # Delete at the beginning
            sll.del_begin()
        elif command == "DE":  # Delete at the end
            sll.del_end()
        elif command == "AP":  # Add at position
            sll.insert_position(int(s[1]), int(s[2]))
        elif command == "DP":  # Delete at position
            sll.del_position(int(s[1]))
        elif command == "TR":  # Traverse the list
            print("Traversal:", sll.traversal())