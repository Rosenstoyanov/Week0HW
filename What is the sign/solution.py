def what_is_my_sign(day, month):
	dayM = day + (month * 40)
	if 21 + (3 * 40) < dayM and dayM < 20 + (4 * 40):
		return "Aries"
	if 21 + (4 * 40) < dayM and dayM < 21 + (5 * 40):
		return "Taurus"
	if 22 + (5 * 40) < dayM and dayM < 21 + (6 * 40):
		return "Gemini"
	if 22 + (6 * 40) < dayM and dayM < 22 + (7 * 40):
		return "Cancer"
	if 23 + (7 * 40) < dayM and dayM < 22 + (8 * 40):
		return "Leo"
	if 23 + (8 * 40) < dayM and dayM < 23 + (9 * 40):
		return "Virgo"
	if 24 + (9 * 40) < dayM and dayM < 23 + (10 * 40):
		return "Libra"
	if 24 + (10 * 40) < dayM and dayM < 22 + (11 * 40):
		return "Scorpio"
	if 23 + (11 * 40) < dayM and dayM < 21 + (12 * 40):
		return "Sagittarius"
	if 21 + (1 * 40) < dayM and dayM < 19 + (2 * 40):
		return "Aquarius"
	if 20 + (2 * 40) < dayM and dayM < 20 + (3 * 40):
		return "Pisces"
