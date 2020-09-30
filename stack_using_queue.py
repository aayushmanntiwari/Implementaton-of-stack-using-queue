'''Implementation of  the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
'''

class Stack:
    def __init__(self):
        self.items = []
     
    def push(self,item):
	 """
        Push element x onto stack.
     """
	 	self.items.insert(0,item)
	 	#self.items.append(item) #originally
    
    def pop(self): 
	 """
        Removes the element on top of the stack and returns that element.
     """
	 	return self.items.pop(0) # where 0 is the index 

	 	#return self.items.pop() #originally
     
    def top(self):
	 """
        Get the top element.
     """
		return self.items[0] 
     	
    def is_empty(self):
		 """
      		Returns whether the stack is empty.
     	"""
		if self.items == []:
	   		return True
		return False 
     
    def size(self):
	 	"""
       		Returns the size of stack.
     	"""
		return len(self.items)
  
S = Stack()

S.push(1)
S.push(2)

print(self.items) [2,1]

print(S.top()) #2

print(S.pop()) #2

print(S.pop()) #1

print(S.is_empty()) #False





	