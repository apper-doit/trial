class cgpio:
	def __init__(self,anos,cathos):
		self.xpins = anos
		self.ypins = cathos

		for i in self.xpins:
			print(i)

		for i in self.ypins:
			print(i)

	def show_box(self,showdata):
		for x in showdata:
			print(x)


	def show_clear(self):
		for x in self.xpins:
			#print(x)
			for y in self.ypins:
				print(x,":",y)
