#banana_verify("BANANA","AAANNB","", ['P', 'M','P', 'M','P', 'M', 'G', 'G', 'G'])
#banana_verify("CAT", "ACT", "", ['P', 'M', 'G', 'M'])
class Stack:
  def __init__(self):
    self.items = []
    
  def isEmpty(self):
    return len(self.items)==0 
  
  def push(self, item):
    self.items.append(item)
  
  def pop(self):
    return self.items.pop() 
  
  def peek(self):
    if not self.isEmpty():
      return self.items[len(self.items)-1]
    
  def size(self):
    return len(self.items) 