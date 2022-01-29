import numpy as np
import random
import keyboard
from time import sleep
from os import system, name

# Define the 4 possible actions on the grid
# Up
def up(mat, score) :
	matrice = mat.copy()
	for z in range(4) :
		for j in range(4) :
			for i in range(3) :
				if z != 2 :
					if matrice[i, j] == 0 :
						matrice[i, j] = matrice[i+1, j]
						matrice[i+1, j] = 0
				else :
					if matrice[i, j] == matrice[i+1, j] :
						score += matrice[i, j] * 2
						matrice[i, j] = matrice[i, j] * 2
						matrice[i+1, j] = 0
	return matrice, score


# Down
def down(mat, score) :
	matrice = mat.copy()
	for z in range(4) :
		for j in range(4) :
			for i in range(3) :
				if z!= 2 :
					if matrice[3-i, j] == 0 :
						matrice[3-i, j] = matrice[3-(i+1), j]
						matrice[3-(i+1), j] = 0
				else :
					if matrice[3-i, j] == matrice[3-(i+1), j] :
						score += matrice[3-i, j] * 2
						matrice[3-i, j] = matrice[3-i, j] * 2
						matrice[3-(i+1), j] = 0
	return matrice, score


# Right
def right(mat, score) :
	matrice = mat.copy()
	for z in range(4) :
		for i in range(4) :
			for j in range(3) :
				if z != 2 :
					if matrice[i, 3-j] == 0 :
						matrice[i, 3-j] = matrice[i, 3-(j+1)]
						matrice[i, 3-(j+1)] = 0
				else :
					if matrice[i, 3-j] == matrice[i, 3-(j+1)] :
						score += matrice[i, 3-j] * 2
						matrice[i, 3-j] = matrice[i, 3-j] * 2
						matrice[i, 3-(j+1)] = 0
	return matrice, score


# Left
def left(mat, score) :
	matrice = mat.copy()
	for z in range(4) :
		for i in range(4) :
			for j in range(3) :
				if z != 2 :
					if matrice[i, j] == 0 :
						matrice[i, j] = matrice[i, j+1]
						matrice[i, j+1] = 0
				else :
					if matrice[i, j] == matrice[i, j+1] :
						score += matrice[i, j] * 2
						matrice[i, j] = matrice[i, j] * 2
						matrice[i, j+1] = 0
	return matrice, score


# Search the 0 in the matrice, pick one at random and replace it by 2 or 4
def rand(mat) :
	w = np.where(mat == 0)
	l = len(w[0])
	
	if l != 0 : # To avoid index out of range
		r = random.choice(range(l))
		if random.random() < 0.8 :
			mat[w[0][r] , w[1][r]] = 2
		else :
			mat[w[0][r] , w[1][r]] = 4
	return mat


# Clear screen
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Save game
def save(mat, score) :
	try :
		with open("/home/kali/Documents/2048_save/save.txt", 'w') as s :
			for j in range(len(mat)) :
				for i in mat[j] :
					s.write(str(i) + "\n")
			s.write(str(score) + "\n")
	except IOError :
		clear()
		print("Save file error")


#Load game
def load() :

	mat = np.array([[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]])
	score = 0
	
	try :
		with open("/home/kali/Documents/2048_save/save.txt", 'r') as l :
			for i in range (4) :
				for j in range(4) :
					mat[i, j] = int(l.readline())
			score = int(l.readline())
	except IOError :
		clear()
		print("Save file error")
	return mat, score


# Draw the state of the game using the matrice
def draw(mat, score) :
	
	# Create the raw game board
	square = [" .-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------. ",
		"| .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |                                            | |                                            | |                                            | |                                            | |",
		"| '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' |",
		"| .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |                                            | |                                            | |                                            | |                                            | |",
		"| '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' |",
		"| .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |                                            | |                                            | |                                            | |                                            | |",
		"| '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' |",
		"| .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. .--------------------------------------------. |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |",
		"| |                                            | |                                            | |                                            | |                                            | |",
		"| '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' '--------------------------------------------' |",
		" '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------' ",
		"  ___  ___ ___  ___ ___   _  ",
		" / __|/ __/ _ \| _ \ __| (_) ",
		" \__ \ (_| (_) |   / _|   _  ",
		" |___/\___\___/|_|_\___| (_) "]
	
	# Draw matrice
	# Add number parts to the list of strings according to their placement in the matrice
	for j in range(4) :
		for i in range(4) :
			if mat[i, j] == 0 :
				square[2 + 9 * i] += "                                            | |"
				square[3 + 9 * i] += "                                            | |"
				square[4 + 9 * i] += "                                            | |"
				square[5 + 9 * i] += "                                            | |"
				square[6 + 9 * i] += "                                            | |"
				square[7 + 9 * i] += "                                            | |"
			elif mat[i, j] == 2 :
				square[2 + 9 * i] += "                    ___                     | |"
				square[3 + 9 * i] += "                   |__ \                    | |"
				square[4 + 9 * i] += "                      ) |                   | |"
				square[5 + 9 * i] += "                     / /                    | |"
				square[6 + 9 * i] += "                    / /_                    | |"
				square[7 + 9 * i] += "                   |____|                   | |"
			elif mat[i, j] == 4 :
				square[2 + 9 * i] += "                   _  _                     | |"
				square[3 + 9 * i] += "                  | || |                    | |"
				square[4 + 9 * i] += "                  | || |_                   | |"
				square[5 + 9 * i] += "                  |__   _|                  | |"
				square[6 + 9 * i] += "                     | |                    | |"
				square[7 + 9 * i] += "                     |_|                    | |"
			elif mat[i, j] == 8 :
				square[2 + 9 * i] += "                    ___                     | |"
				square[3 + 9 * i] += "                   / _ \                    | |"
				square[4 + 9 * i] += "                  | (_) |                   | |"
				square[5 + 9 * i] += "                   > _ <                    | |"
				square[6 + 9 * i] += "                  | (_) |                   | |"
				square[7 + 9 * i] += "                   \___/                    | |"
			elif mat[i, j] == 16 :
				square[2 + 9 * i] += "                 __     __                  | |"
				square[3 + 9 * i] += "                /_ |   / /                  | |"
				square[4 + 9 * i] += "                 | |  / /_                  | |"
				square[5 + 9 * i] += "                 | | | '_ \                 | |"
				square[6 + 9 * i] += "                 | | | (_) |                | |"
				square[7 + 9 * i] += "                 |_|  \___/                 | |"
			elif mat[i, j] == 32 :
				square[2 + 9 * i] += "                ____    ___                 | |"
				square[3 + 9 * i] += "               |___ \  |__ \                | |"
				square[4 + 9 * i] += "                 __) |    ) |               | |"
				square[5 + 9 * i] += "                |__ <    / /                | |"
				square[6 + 9 * i] += "                ___) |  / /_                | |"
				square[7 + 9 * i] += "               |____/  |____|               | |"
			elif mat[i, j] == 64 :
				square[2 + 9 * i] += "                 __    _  _                 | |"
				square[3 + 9 * i] += "                / /   | || |                | |"
				square[4 + 9 * i] += "               / /_   | || |_               | |"
				square[5 + 9 * i] += "              | '_ \  |__   _|              | |"
				square[6 + 9 * i] += "              | (_) |    | |                | |"
				square[7 + 9 * i] += "               \___/     |_|                | |"
			elif mat[i, j] == 128 :
				square[2 + 9 * i] += "              __   ___     ___              | |"
				square[3 + 9 * i] += "             /_ | |__ \   / _ \             | |"
				square[4 + 9 * i] += "              | |    ) | | (_) |            | |"
				square[5 + 9 * i] += "              | |   / /   > _ <             | |"
				square[6 + 9 * i] += "              | |  / /_  | (_) |            | |"
				square[7 + 9 * i] += "              |_| |____|  \___/             | |"
			elif mat[i, j] == 256 :
				square[2 + 9 * i] += "            ___    _____     __             | |"
				square[3 + 9 * i] += "           |__ \  | ____|   / /             | |"
				square[4 + 9 * i] += "              ) | | |__    / /_             | |"
				square[5 + 9 * i] += "             / /  |___ \  | '_ \            | |"
				square[6 + 9 * i] += "            / /_   ___) | | (_) |           | |"
				square[7 + 9 * i] += "           |____| |____/   \___/            | |"
			elif mat[i, j] == 512 :
				square[2 + 9 * i] += "              _____   __   ___              | |"
				square[3 + 9 * i] += "             | ____| /_ | |__ \             | |"
				square[4 + 9 * i] += "             | |__    | |    ) |            | |"
				square[5 + 9 * i] += "             |___ \   | |   / /             | |"
				square[6 + 9 * i] += "              ___) |  | |  / /_             | |"
				square[7 + 9 * i] += "             |____/   |_| |____|            | |"
			elif mat[i, j] == 1024 :
				square[2 + 9 * i] += "          __    ___    ___    _  _          | |"
				square[3 + 9 * i] += "         /_ |  / _ \  |__ \  | || |         | |"
				square[4 + 9 * i] += "          | | | | | |    ) | | || |_        | |"
				square[5 + 9 * i] += "          | | | | | |   / /  |__   _|       | |"
				square[6 + 9 * i] += "          | | | |_| |  / /_     | |         | |"
				square[7 + 9 * i] += "          |_|  \___/  |____|    |_|         | |"
			elif mat[i, j] == 2048 :
				square[2 + 9 * i] += "        ___     ___    _  _      ___        | |"
				square[3 + 9 * i] += "       |__ \   / _ \  | || |    / _ \       | |"
				square[4 + 9 * i] += "          ) | | | | | | || |_  | (_) |      | |"
				square[5 + 9 * i] += "         / /  | | | | |__   _|  > _ <       | |"
				square[6 + 9 * i] += "        / /_  | |_| |    | |   | (_) |      | |"
				square[7 + 9 * i] += "       |____|  \___/     |_|    \___/       | |"
			elif mat[i, j] == 4096 :
				square[2 + 9 * i] += "       _  _      ___     ___      __        | |"
				square[3 + 9 * i] += "      | || |    / _ \   / _ \    / /        | |"
				square[4 + 9 * i] += "      | || |_  | | | | | (_) |  / /_        | |"
				square[5 + 9 * i] += "      |__   _| | | | |  \__, | | '_ \       | |"
				square[6 + 9 * i] += "         | |   | |_| |    / /  | (_) |      | |"
				square[7 + 9 * i] += "         |_|    \___/    /_/    \___/       | |"
			elif mat[i, j] == 8192 :
				square[2 + 9 * i] += "          ___    __    ___    ___           | |"
				square[3 + 9 * i] += "         / _ \  /_ |  / _ \  |__ \          | |"
				square[4 + 9 * i] += "        | (_) |  | | | (_) |    ) |         | |"
				square[5 + 9 * i] += "         > _ <   | |  \__, |   / /          | |"
				square[6 + 9 * i] += "        | (_) |  | |    / /   / /_          | |"
				square[7 + 9 * i] += "         \___/   |_|   /_/   |____|         | |"
			elif mat[i, j] == 16384 :
				square[2 + 9 * i] += "    __     __    ____     ___    _  _       | |"
				square[3 + 9 * i] += "   /_ |   / /   |___ \   / _ \  | || |      | |"
				square[4 + 9 * i] += "    | |  / /_     __) | | (_) | | || |_     | |"
				square[5 + 9 * i] += "    | | | '_ \   |__ <   > _ <  |__   _|    | |"
				square[6 + 9 * i] += "    | | | (_) |  ___) | | (_) |    | |      | |"
				square[7 + 9 * i] += "    |_|  \___/  |____/   \___/     |_|      | |"
			elif mat[i, j] == 32768 :
				square[2 + 9 * i] += "   ____    ___    ______     __     ___     | |"
				square[3 + 9 * i] += "  |___ \  |__ \  |____  |   / /    / _ \    | |"
				square[4 + 9 * i] += "    __) |    ) |     / /   / /_   | (_) |   | |"
				square[5 + 9 * i] += "   |__ <    / /     / /   | '_ \   > _ <    | |"
				square[6 + 9 * i] += "   ___) |  / /_    / /    | (_) | | (_) |   | |"
				square[7 + 9 * i] += "  |____/  |____|  /_/      \___/   \___/    | |"
			elif mat[i, j] == 65536 :
				square[2 + 9 * i] += "     __    _____   _____   ____      __     | |"
				square[3 + 9 * i] += "    / /   | ____| | ____| |___ \    / /     | |"
				square[4 + 9 * i] += "   / /_   | |__   | |__     __) |  / /_     | |"
				square[5 + 9 * i] += "  | '_ \  |___ \  |___ \   |__ <  | '_ \    | |"
				square[6 + 9 * i] += "  | (_) |  ___) |  ___) |  ___) | | (_) |   | |"
				square[7 + 9 * i] += "   \___/  |____/  |____/  |____/   \___/    | |"
	
	#Draw Score
	beg = True
	for i in range(9, -1, -1) :
		c = int(score / 10**i) % 10
		if c == 0 and not beg or score == 0 :
			square[38] += "  __   "
			square[39] += " /  \  "
			square[40] += "| () | "
			square[41] += " \__/  "
			if score == 0 :
				break
		
		elif c == 1 :
			square[38] += " _  "
			square[39] += "/ | "
			square[40] += "| | "
			square[41] += "|_| "
			beg = False
		
		elif c == 2 :
			square[38] += " ___  "
			square[39] += "|_  ) "
			square[40] += " / /  "
			square[41] += "/___| "
			beg = False

		elif c == 3 :
			square[38] += " ____ "
			square[39] += "|__ / "
			square[40] += " |_ \ "
			square[41] += "|___/ "
			beg = False
		
		elif c == 4 :
			square[38] += " _ _   "
			square[39] += "| | |  "
			square[40] += "|_  _| "
			square[41] += "  |_|  "
			beg = False
		
		elif c == 5 :
			square[38] += " ___  "
			square[39] += "| __| "
			square[40] += "|__ \ "
			square[41] += "|___/ "
			beg = False
		
		elif c == 6 :
			square[38] += "  __  "
			square[39] += " / /  "
			square[40] += "/ _ \ "
			square[41] += "\___/ "
			beg = False

		elif c == 7 :
			square[38] += " ____  "
			square[39] += "|__  | "
			square[40] += "  / /  "
			square[41] += " /_/   "
			beg = False
		
		elif c == 8 :
			square[38] += " ___  "
			square[39] += "( _ ) "
			square[40] += "/ _ \ "
			square[41] += "\___/ "
			beg = False
		
		elif c == 9 :
			square[38] += " ___  "
			square[39] += "/ _ \ "
			square[40] += "\_  / "
			square[41] += " /_/  "
			beg = False
	
	# Draw the entire board by printing the list of strings
	for k in range(len(square)) :
		print(square[k])


# Variable initialization :
def init() :
	global mat2
	mat2 = np.array([[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]])
	rand(mat2)
	rand(mat2)
	global score
	score = 0
	return mat2, score


# Game loop
def game(mat2, score) :
	carry_on = True
	while carry_on :
		
		clear()
		draw(mat2, score)
		sleep(0.2)
		mat1 = mat2.copy()
		
		key = keyboard.read_key()
		
		if key == "up" :
			m = up(mat1, score)
			mat2 = m[0]
			score = m[1]
			if game_over(mat2, score) :
				carry_on = False
			if not np.array_equiv(mat1, mat2) :
				rand(mat2)
	
		elif key == "down" :
			m = down(mat1, score)
			mat2 = m[0]
			score = m[1]
			if game_over(mat2, score) :
				carry_on = False
			if not np.array_equiv(mat1, mat2) :
				rand(mat2)
	
		elif key == "right" :
			m = right(mat1, score)
			mat2 = m[0]
			score = m[1]
			if game_over(mat2, score) :
				carry_on = False
			if not np.array_equiv(mat1, mat2) :
				rand(mat2)
	
		elif key == "left" :
			m = left(mat1, score)
			mat2 = m[0]
			score = m[1]
			if game_over(mat2, score) :
				carry_on = False
			if not np.array_equiv(mat1, mat2) :
				rand(mat2)
		
		elif key == "l" :
			loa = load()
			mat2 = loa[0]
			score = loa[1]
	
		elif key == "s" :
			save(mat2, score)

		elif key == "esc" :
			carry_on = False


# End
def game_over(mat, score) :
	if np.array_equiv(mat, up(mat, 0)[0]) and np.array_equiv(mat, down(mat, 0)[0]) and np.array_equiv(mat, right(mat, 0)[0]) and np.array_equiv(mat, left(mat, 0)[0]) :
		clear()
		print("""
		
		
		
		   ______       _      ____    ____ ________     ___   ____   ____ ________ _______     
		 .' ___  |     / \    |_   \  /   _|_   __  |  .'   `.|_  _| |_  _|_   __  |_   __ \    
		/ .'   \_|    / _ \     |   \/   |   | |_ \_| /  .-.  \ \ \   / /   | |_ \_| | |__) |   
		| |   ____   / ___ \    | |\  /| |   |  _| _  | |   | |  \ \ / /    |  _| _  |  __ /    
		\ `.___]  |_/ /   \ \_ _| |_\/_| |_ _| |__/ | \  `-'  /   \ ' /    _| |__/ |_| |  \ \_  
		 `._____.'|____| |____|_____||_____|________|  `.___.'     \_/    |________|____| |___| 
		 
		""")
		print("                                               Your final score is : " + str(score))
		sleep(1)
		keyboard.read_key()
		return True
	else :
		return False



# Help
def help() :
	clear()
	print("""
	 .---------------------------------------------------------------------------. 
	| .-------------------------------------------------------------------------. |
	| |                                                                         | |
	| |       The goal of the game is to make 2048 by merging the numbers.      | |
	| |                      Two 2 make 4, two 4 make 8...                      | |
	| |                                                                         | |
	| |      Use the arrows ← ↑ → ↓ to push all numbers to one side of the      | |
	| |                     grid and merge similar numbers.                     | |
	| |                                                                         | |
	| |       This is game over when the grid is full and no more numbers       | |
	| |                             can be merge.                               | |
	| |                                                                         | |
	| |       You can use 's' to save and 'l' to load state at any moment.      | |
	| |                                                                         | |
	| |          Press 'esc' when you're done with this stupid game :p          | |
	| |                                                                         | |
	| |                         Otherwise... Enjoy !                            | |
	| |                                                                         | |
	| |                                                    Alsip                | |
	| |                                                                         | |
	| '-------------------------------------------------------------------------' |
	 '---------------------------------------------------------------------------' 
	""")
	sleep(1)
	keyboard.read_key()


# Main
def main() :
	menu = True
	while menu :
		clear()
		print("""
	
	
	
	
		   222222222222222          000000000             444444444        888888888     
		  2:::::::::::::::22      00:::::::::00          4::::::::4      88:::::::::88   
		  2::::::222222:::::2   00:::::::::::::00       4:::::::::4    88:::::::::::::88 
		  2222222     2:::::2  0:::::::000:::::::0     4::::44::::4   8::::::88888::::::8
		              2:::::2  0::::::0   0::::::0    4::::4 4::::4   8:::::8     8:::::8
		              2:::::2  0:::::0     0:::::0   4::::4  4::::4   8:::::8     8:::::8
		           2222::::2   0:::::0     0:::::0  4::::4   4::::4    8:::::88888:::::8 
		      22222::::::22    0:::::0 000 0:::::0 4::::444444::::444   8:::::::::::::8  
		    22::::::::222      0:::::0 000 0:::::0 4::::::::::::::::4  8:::::88888:::::8 
		   2:::::22222         0:::::0     0:::::0 4444444444:::::444 8:::::8     8:::::8
		  2:::::2              0:::::0     0:::::0           4::::4   8:::::8     8:::::8
		  2:::::2              0::::::0   0::::::0           4::::4   8:::::8     8:::::8
		  2:::::2       222222 0:::::::000:::::::0           4::::4   8::::::88888::::::8
		  2::::::2222222:::::2  00:::::::::::::00          44::::::44  88:::::::::::::88 
		  2::::::::::::::::::2    00:::::::::00            4::::::::4    88:::::::::88   
		  22222222222222222222      000000000              4444444444      888888888     
	  
	  
	  
					  	Press s to start a new game
	  					Press l to load game
	  					Press h to learn how to play
	  					Press esc to exit
	  	
	""")
	
		sleep(0.2)
	
		choice = keyboard.read_key()
	
		if choice == "s" :
			ini = init()
			game(ini[0], ini[1])
	
		elif choice == "l" :
			loa = load()
			game(loa[0], loa[1])
			
		elif choice == "h" :
			help()
		
		elif choice == "esc" :
			menu = False


if __name__ == "__main__":
	main()
	print("\n\nbye !")