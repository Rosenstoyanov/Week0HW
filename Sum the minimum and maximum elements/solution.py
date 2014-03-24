def sum_of_min_and_max(arr):
	maxel = 0

	for item in arr:
		if item > maxel:
			maxel = item
	minel = maxel
	for item in arr:
		if item < minel:
			minel = item

	return minel + maxel
