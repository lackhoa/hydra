from Hydra import Hydra

class TitHydra(Hydra):
	def __init__(self):
		self.heads = ['0']
	
	def clean(self):
		for head in self.heads:
			head = ['0']

	def spawn(self):
		self.heads.insert(0, '1')

	def mutate(self):
		clean = True

		for i in reversed(range(len(self.heads))):
			if self.heads[i] == '0':
				self.heads[i] = '1'
				clean = False
				break
			elif self.heads[i] == '1':
				self.heads[i] = '2'
				clean = False
				break
			elif self.heads[i] == '2':
				self.heads[i] = '0'

		if clean:
			self.clean()
			self.spawn()

# MAIN
superTitHydra = TitHydra()
for _ in range(10):
	print(superTitHydra.to_string())
	superTitHydra.mutate()