import random

# setting difficulty levels 
# difficulty = 0 easy
# difficulty = 1 hard
difficulty = 0
symbol = 0
computer_symbol = 0
symbols = ['O', 'X', " "]
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

# void function to print a board with relevant formatting
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

def pickposition(hard, board):
	available_positions = []
	for i in range(len(board)):
		if board[i] == 2:
			available_positions.append(i)
	if hard == False:
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
		return random.choice(available_positions)

def check_win(symbol, board):
	for combination in possible_combinations:
		if(board[combination[0]] == symbol == board[combination[1]] == board[combination[2]]):
			return True
	return False;

def check_result(s, board):
	if(check_win(s, board)):
		return 1
	if(check_win(s^1, board)):
		return 0
	if(board.count(2) == 0):
		return 2
	return -1

print("Set game difficulty")
while True:
	difficulty_input = input("Enter 'EASY' or 'HARD': ")
	difficulty_input = difficulty_input.upper()
	if difficulty_input == "EASY":
		difficulty = 0
		break
	elif difficulty_input == "HARD":
		difficulty = 1
		break
	else: 
		print("Invalid input, please try again.")

print("Pick your symbol!")
while True:
	symbol_input = input("Enter 'O' or 'X': ")
	symbol_input = symbol_input.upper()
	if symbol_input == "O":
		symbol = 0
		break
	elif symbol_input == "X":
		symbol = 1
		break
	else: 
		print("Invalid input, please try again.")

computer_symbol = symbol ^ 1
print("Starting the game!")
gameboard = [2, 2, 2, 2, 2, 2, 2, 2, 2]
while True:
	# check for game ending 
	result = check_result(symbol, gameboard)
	if result == 1:
		print("You win! Well played!")
		break
	elif result == 0:
		print("You lost, feel free to try again!")
		break
	elif result == 2:
		print("It's a draw! Good game!")
		break

	print("You can do one of the following operations: ")
	print("- LEGEND, display the position legend for the board.")
	print("- BOARD, diplay the current game board.")
	print("- MOVE, move ")
	user_input = input("Enter 'LEGEND', 'BOARD', 'MOVE': ")
	user_input = user_input.upper();
	if user_input == "LEGEND":
		printboard(gameboard, True)
	elif user_input == 'BOARD':
		printboard(gameboard, False)
	elif user_input == 'MOVE':
		print("Game position legend: ")
		printboard(gameboard, True)
		print("Current game board: ")
		printboard(gameboard, False)
		while True:
			user_move = input("Enter position [0—8]: ")
			if user_move.isnumeric() == False:
				print("Invalid input, please try again.")
				continue
			user_move = int(user_move)
			if user_move >= 0 and user_move < 9:
				if gameboard[user_move] != 2:
					print("Position already taken, please try again.")
					continue
				else:
					print(f"You played {symbols[symbol]} at the position {user_move}, here is the resulting board:")
					gameboard[user_move] = symbol;
					printboard(gameboard, False)
					break
			else:
				print("Invalid input, please try again.")
				continue
		result = check_result(symbol, gameboard)
		if result == 1:
			print("You win! Well played!")
			break
		elif result == 0:
			print("You lose, feel free to try again!")
			break
		elif result == 2:
			print("It's a draw! Good game!")
			break
		computer_move = pickposition(difficulty, gameboard)
		print(f"The computer played {symbols[computer_symbol]} at the position {computer_move}, here is the resulting board:")
		gameboard[computer_move] = computer_symbol
		printboard(gameboard, False)

	else:
		print("Invalid input, please try again.")
	print()
