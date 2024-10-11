import random

def initialization(s, e):
	sn = random.randint(s, e)
	return sn

def start_game(sn, s, e):
	guess = eval(input(f"Guess the number between {s} to {e}: "))
	return guess == sn
	
def stop_game(status):
	if status:
		print("Win")
	else:
		print("Loss")

def guess_the_number():
	sn = initialization(1, 20)
	status = start_game(sn, 1, 20)
	stop_game(status)
	
guess_the_number()
