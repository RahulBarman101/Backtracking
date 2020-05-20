import numpy as np

board = np.zeros((4,4))
N = 4
# print(board)
def solve(n):
	result = []

	def dfs(queens,xy_dif,xy_sum):

		'''
		queens: list of occupied positions by the queens
		xy_dif,xy_sum: list to find the diagonals of the queens occupied
		'''
		p = len(queens)
		print()
		# print(f'len is {p}')
		# print()
		# print(f'queens list is {queens}')
		# print()
		# print(f'xy diff is {xy_dif}')
		# print()
		# print(f'xy sum is {xy_sum}')
		if p == n:
			result.append(queens)
			return

		for q in range(n):
			if not q in queens and p-q not in xy_dif and p+q not in xy_sum:
				dfs(queens+[q],xy_dif+[p-q],xy_sum+[p+q])


	dfs([],[],[])
	col = 0
	for i in result[0]:
		board[i][col] = 1
		col+=1


solve(N)
print(board)