class link:
	def __init__(self, data):
		self.data = data
		self.nextlink = None
		self.previouslink = None

class chain:
	def __init__(self):
		self.beginlink = None
		self.endlink = None
		self.length = 0
	def addlink(self, data):
		newlink = link(data)
		self.length += 1
		if self.beginlink is None:
			self.beginlink = self.endlink = newlink
		else:
			newlink.previouslink = self.endlink
			self.endlink.nextlink = newlink
			self.endlink = newlink
	def get_index(self, index):
		if index >= 0:
			currentlink = self.beginlink
			for i in range(index):
				currentlink = currentlink.nextlink
			return currentlink.data
		elif index == -1:
			return self.endlink.data

if __name__ == "__main__":
	import time
	start = time.time()
	newlist = chain()
	
	n = 8000000
	for i in range(n):
		newlist.addlink(i)
	
	for i in range(newlist.length):
		if i == 7999999:
			print(newlist.get_index(i))
			endtime = time.time()
	print(f"{endtime - start} seconds")
