def slope_style_score(scores):
	minItem = min(scores)
	maxItem = max(scores)
	sumElem = 0
	for item in scores:
		sumElem += item
	sumElem -= minItem
	sumElem -= maxItem
	return sumElem/3
