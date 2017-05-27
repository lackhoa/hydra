class Hydra:
	def __init__(self):
		raise NotImplementedError

	def clean(self):
		"""
		Set all the heads to the original state
		"""
		pass

	def spawn(self):
		"""
		Spawn a new head
		"""
		pass

	def mutate(self):
		"""
		Mutate to the next state
		"""
		pass

	def to_string(self):
		ans = ''
		for head in self.heads:
			ans += head
		return ans