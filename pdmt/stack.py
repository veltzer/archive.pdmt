class Stack(object):
	def __init__(self):
		self.storage = list()
	def isEmpty(self):
		return not self.storage
	def push(self,p):
		self.storage.append(p)
	def pop(self):
		return self.storage.pop()
	def foreach(self):
		for x in self.storage:
			yield x

if __name__ == '__main__':
	s=Stack()
	s.push(3)
	s.push(4)
	s.push(5)
	for x in s.foreach():
		print(x)
	print(s.pop());
	print(s.pop());
	print(s.pop());
	print(s.pop());
