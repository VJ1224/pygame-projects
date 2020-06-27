#Python program to solve a sudoku game

#displays the board
def print_board(board):
	for i in range(9):
		for j in range(9):
			#prints the cell with a space after
			print (board[i][j]," ",end="")
			#after every 3 cells prints a |
			if((j+1)%3==0):
				print("| ",end="")
		#prints a dashed line after every 3 cells
		if((i+1)%3==0):
			print("\n")
			print("-"*32)
		#prints new line
		else:
			print("\n")

def check(board,pos,num):
	# row
	for i in range(len(board[0])):
		if board[pos[0]][i] == num and pos[1] != i:
			return False

	# col
	for i in range(len(board)):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	x_box = pos[1] // 3
	y_box = pos[0] // 3

	for i in range(y_box * 3, y_box * 3 + 3):
		for j in range(x_box * 3, x_box * 3 + 3):
			if board[i][j] == num and (i,j) != pos:
				return False

	return True

#finds an empty cell to solve
def find_empty(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i,j)
	return None

#solves the puzzle using backtracking algorithm
def solver(board):
	search = find_empty(board)
	if not search:
		return True
	else:
		row,col = search

	for n in range(1,10):
		if (check(board,(row,col),n)):
			board[row][col] = n
			if(solver(board)):
				return True
			board[row][col]=0
	return False
