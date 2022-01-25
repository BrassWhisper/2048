import keyboard
from time import sleep

while True :
	
	key = keyboard.read_key()
	
	if key == "up" :
		up(mat)

	elif key == "down" :
		down(mat)

	elif key == "right" :
		right(mat)

	elif key == "left" :
		left(mat)

	elif key == "esc" :
		break

	clear()
	draw(mat)
	sleep(0.5)