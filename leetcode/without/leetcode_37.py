'''
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.
You may assume that there will be only one unique solution.
'''

def solverSudoku(board):
	pass





list1 = ['53..7....',
		'6..195...',
		 '.98....6.',
		 '8...6...3',
		 '4..8.3..1',
		 '7...2...6',
	 	'.6....28.',
		 '...419..5',
		 '....8..79']



a = [1,2,3,4,5,6,7,8,9]
b = [3,6,8,9]
for i in (set(a)-set(b)):
	print(type(i))
l = ['123456','5678']
print(l[0].replace(l[0][2],'c'))
print(l[0])
z = 'abc'
print(z.replace('a','jjj'))
print(z)