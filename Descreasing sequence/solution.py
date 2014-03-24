def is_decreasing(seq):
	for x in range(1,len(seq)):
		if seq[x - 1] > seq[x]:
			return True
		else: return False
