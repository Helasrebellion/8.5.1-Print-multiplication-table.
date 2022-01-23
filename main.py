user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

''' Your solution goes here '''
for lst in mult_table:
	for i in range(len(lst)):
		print(lst[i],end='')
		if i!=len(lst)-1:
			print(' | ',end='')
	print()
