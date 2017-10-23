
def stackperm(lst):

	def perm(element,stack_or_):
		yield element

	stack = []
	for i,j in enumerate(lst):
		perm(j)