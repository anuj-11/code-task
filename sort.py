data_list = [10, 23, 34, 40, 12, 2, 15]
new_list = []
while data_list:
	minimum = data_list[0]
	for x in data_list:
		if x < minimum:
			minimum = x
	new_list.append(minimum)
	data_list.remove(minimum)
print new_list
