def ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))

	def recursive(day):
		if day > days:
			print("Harvest time!")
			return
		print("Day", day)
		recursive(day + 1)
	recursive(1)

