''' this backtracking algorithm based on three basic functions one for searching '''

print("\n")
global Queens 
Queens = int(input("please enter the number of queens ")) # number of queens taken from the user  

print("\n")
solCounter=1 #variable for the number of possible solutions if found 

''' function for cheking the constrains of the Nqueens and it's position 
this function works from the left side of the board till the write as it starts from column 0 till column-1
we call this function after placing queen in col to start cheking its place '''
def CheckSafty(NQueensBoard, row, col) :
	
	# this check row on left side by moving in all coumns in this row to found if it's empty
	for i in range(col): 
		if (NQueensBoard[row][i]): 
			return False 

	# this check upper diagonal on left side 
	i = row
	j = col
	while i >= 0 and j >= 0:
		if(NQueensBoard[i][j]):
			return False
		i -= 1
		j -= 1

	# this check upper diagonal on left side 
	i = row
	j = col
	while j >= 0 and i < Queens:
		if(NQueensBoard[i][j]):
			return False
		i = i + 1
		j = j - 1

	return True

# this function is for printing the solution in a matrix with the possible places for each queen
def PossibelSolution(NQueensBoard): 
	global solCounter 
	print("solution number ",solCounter)
	solCounter = solCounter + 1
	#for loop for printing the queens in a matrix way 
	for i in range(Queens): 
		for j in range(Queens):
			print(NQueensBoard[i][j], end = " ")
		print("\n")
	print("\n") 

''' This is the function where we are making our decision
 for the queens position accounrding to this puzzel constrain 
 by returning true if their is possible solutions or false '''
def SolvedOrNot(NQueensBoard, col) :
    # This checks if all the queens are aready set if true calling the print function the solution	
	if (col == Queens): 
		PossibelSolution(NQueensBoard) 
		return True

	'''else placing the queen in all rows one by one in the same column 
       so that to found it's place  '''
	
	Sol = False #variable to return if queen is set in possible position or not  

	for i in range(Queens):
			
		''' calling check safty function to show if queen can be placed in this
          position or not if safty board[i][col] so that we place it in the board by 1  '''

		if (CheckSafty(NQueensBoard, i, col)): 
		
			NQueensBoard[i][col] = "q" #matrix place will contain q if queen follow the rules of the game  

			Sol = SolvedOrNot(NQueensBoard, col + 1) or Sol #Sol now contain the state of the queen   

			''' If placing queen in board[i][col] 
			doesn't lead to a solution, then 
			remove queen from board[i][col] '''
			NQueensBoard[i][col] = 0 # this column will be backtracked till it goes to safe situation 
		
	''' If queen can not be place in any row in 
		this column col then return false '''
	return Sol

def QueenMatrix() :

	NQueensBoard = [[0 for j in range(8)] 
				for i in range(8)]

	if (SolvedOrNot(NQueensBoard, 0) == False): #if sol which is returned from SolvedOrNot function is false so that print no solution 
	
		print("Solution not found") 
		return
	return

# main function in which the code starts from
QueenMatrix()