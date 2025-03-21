for row in range(10):
	for column in range(10):

		print('<' if row % 2 == 1 else '>', end='')

	print()



"""
If the row index is odd (row % 2 == 1), it prints <
If the row index is even (row % 2 == 0), it prints >
"""