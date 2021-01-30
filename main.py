"""
Name: Sarthak Mangla
Class: 11J
Summary: 
A tic tac toe game which allows the user to set difficulty and pick their symbol.
"""

# Importing random module for random.choice()
import random 

# Configuration variables 
difficulty = 0 
# Easy = 0
# Hard = 1
symbols = ['O', 'X', " "]
symbol = 0
computer_symbol = 0
# Gameboard - 3x3 square flattened into list of 9 integers
# Universal notation:
# 0 = O 
# 1 = X
# 2 = (empty cell)
# These values can be extracted from the symbols list defined above. 
gameboard = [2, 2, 2, 2, 2, 2, 2, 2, 2]
# List of all possible winning combinations indices
possible_combinations = [
	(0, 3, 6),
	(1, 4, 7),
	(2, 5, 8),
	(0, 1, 2),
	(3, 4, 5),
	(6, 7, 8),
	(0, 4, 8),
	(2, 4, 6)
]

"""
Parameters:
1) board — List of 9 Integers, depicting the game board.
2) legend - Boolean, True if legend is to be printed, False if actual board is to printed. 

Description:
Prints the given board along with relevant formatting.

Return Value:
Void function, does not return anything.
"""
def printboard(board, legend):
	print("––––––––––––—")
	for row in range(3):
		print("| ", end="")
		for col in range(3):
			if legend:
				print((row*3)+col, end=" | ")
			else:
				print(symbols[board[(row*3)+col]], end=" | ")
		print()
		print("––––––––––––—")


"""
Parameters:
1) hard — Boolean value, True if the difficulty is set to hard, otherwise False
2) board - List of 9 Integers, depicting the game board.

Description:
Depending on the state of the board and the difficulty chosen, this function picks an appropiate cell for the computer to move.

Return Value:
Returns the index of the picked cell.
"""
def pickposition(hard, board):
	available_positions = []
	# Finding all available positions
	for i in range(len(board)):
		if board[i] == 2:
			available_positions.append(i)
	if hard == False:
		# Returns random value from available positions
		return random.choice(available_positions)
	else:
		# Checking if one move win is possible
		aux_board = board
		for i in available_positions:
			aux_board[i] = computer_symbol
			if check_win(computer_symbol, aux_board):
				return i
			aux_board[i] = 2
		# Checking if one move loss prevention is possible
		for i in available_positions:
			aux_board[i] = symbol
			if check_win(symbol, aux_board):
				return i
			aux_board[i] = 2
		# If neither is possible, returns random value from available positions
		return random.choice(available_positions)

"""
Parameters:
1) symbol — Integer value, either 0 or 1.
2) board - List of 9 Integers, depicting the game board.

Description:
This function loops through all the possible winning combinations, and checks if any of them are equal to the given symbol.

Return Value:
Returns True if a valid combination found, False otherwise.
"""
def check_win(symbol, board):
	for combination in possible_combinations:
		if(board[combination[0]] == symbol == board[combination[1]] == board[combination[2]]):
			return True
	return False;

"""
Parameters:
1) s — Integer value, (symbol) either 0 or 1.
2) board - List of 9 Integers, depicting the game board.

Description:
Given the board and symbol, checks if the symbol won/lost or the game is tied.

Return Value:
Returns 1 if the symbol 's' won, returns 0 if the symbol 's' lost, returns 2 if the board is a draw, and returns -1 if neither won, lost or draw.
"""
def check_result(s, board):
	# Checking if symbol 's' won
	if(check_win(s, board)):
		return 1
	# Checking if symbol 's' lost
	if(check_win(s^1, board)):
		return 0
	# Checking for draw
	if(board.count(2) == 0):
		return 2
	# Returning -1 if none of the above conditions are true
	return -1

# Setting game difficulty
print("Set game difficulty")
while True:
	# Taking input
	difficulty_input = input("Enter 'EASY' or 'HARD': ")
	# Converting input to uppercase
	difficulty_input = difficulty_input.upper()
	if difficulty_input == "EASY":
		# Setting difficulty variable value
		difficulty = 0
		break
	elif difficulty_input == "HARD":
		# Setting difficulty variable value
		difficulty = 1
		break
	else: 
		# Invalid input
		print("Invalid input, please try again.")

# Allowing the player to pick their symbol
print("Pick your symbol!")
while True:
	# Taking input
	symbol_input = input("Enter 'O' or 'X': ")
	# Converting input to uppercase
	symbol_input = symbol_input.upper()
	if symbol_input == "O":
		# Setting symbol variable value
		symbol = 0
		break
	elif symbol_input == "X":
		# Setting symbol variable value
		symbol = 1
		break
	else: 
		# Invalid input
		print("Invalid input, please try again.")

# Setting opposition (computer) symbol
computer_symbol = symbol ^ 1

# Starting the actual game
print("Starting the game!")
while True:
	# Checking if game has ended
	result = check_result(symbol, gameboard)
	if result == 1:
		# Printing win
		print("You win! Well played!")
		break
	elif result == 0:
		# Printing loss
		print("You lost, feel free to try again!")
		break
	elif result == 2:
		# Printing draw
		print("It's a draw! Good game!")
		break

	# Printing description of all possible operations
	print("You can do one of the following operations: ")
	# LEGEND: displaying the position legend
	print("- LEGEND, display the position legend for the board.")
	# BOARD: displaying the current game board
	print("- BOARD, diplay the current game board.")
	# MOVE: where the player can actually move
	print("- MOVE, move ")
	# Taking input
	user_input = input("Enter 'LEGEND', 'BOARD', 'MOVE': ")
	# Converting input to uppercase
	user_input = user_input.upper();
	if user_input == "LEGEND":
		# Printing legend
		print("Game position legend: ")
		printboard(gameboard, True)
	elif user_input == 'BOARD':
		# Printing gameboard
		print("Current game board: ")
		printboard(gameboard, False)
	elif user_input == 'MOVE':
		# Printing legend
		print("Game position legend: ")
		printboard(gameboard, True)
		# Printing current gameboard
		print("Current game board: ")
		printboard(gameboard, False)
		while True:
			# Taking input
			user_move = input("Enter position [0—8]: ")
			# If input is not numeric, print invalid input
			if user_move.isnumeric() == False:
				# Invalid input
				print("Invalid input, please try again.")
				continue
			# Converting to integer
			user_move = int(user_move)
			# Checking if index is valid
			if user_move >= 0 and user_move < 9:
				# Checking if index is empty
				if gameboard[user_move] != 2:
					print("Position already taken, please try again.")
					continue
				else:
					# Making the actual move
					print(f"You played {symbols[symbol]} at the position {user_move}, here is the resulting board:")
					gameboard[user_move] = symbol;
					# Printing the gameboard after the move
					printboard(gameboard, False)
					break
			else:
				# Invalid input
				print("Invalid input, please try again.")
				continue
		# Checking if game has ended
		result = check_result(symbol, gameboard)
		if result == 1:
			# Printing win
			print("You win! Well played!")
			break
		elif result == 0:
			# Printing loss
			print("You lose, feel free to try again!")
			break
		elif result == 2:
			# Printing draw
			print("It's a draw! Good game!")
			break
		# Selecting computer move
		computer_move = pickposition(difficulty, gameboard)
		# Making the actual move
		print(f"The computer played {symbols[computer_symbol]} at the position {computer_move}, here is the resulting board:")
		gameboard[computer_move] = computer_symbol
		# Printing the gameboard after the move 
		printboard(gameboard, False)

	else:
		# Invalid input
		print("Invalid input, please try again.")
	print()
