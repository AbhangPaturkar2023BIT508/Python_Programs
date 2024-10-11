import random

def initialization():
	rewards = {1 : 5, 2 : 3, 3 : 2, 4 : 1.5, 5 : 1}
	print("---Welcome to Guess the Number Game---")
	print("...YOU CAN WIN UPTO 5x TIME REWARD...")
	print("Rules : ")
	for i in rewards:
		print(f"	Attempt {i} : Win {rewards[i]}x")
	sn = random.randint(1, 100)
	entry_fees = eval(input("Enter Amount : "))
	return sn, rewards, entry_fees

def start_game(sn, rewards, entry_fees):
	for attempt in range(1, 6):
		print(f"Attempt : {attempt}")
		guess = eval(input(f"Guess the number between 1 to 100: {sn} "))
		if guess == sn:
			return entry_fees * rewards[attempt]
		else:
			prediction = guess / sn
			if prediction >= 1.5:
				print("Guess is too large...")
			elif prediction < 1.5 and prediction >= 1:
				print("Guess is large...")
			elif prediction >= 0.5 and prediction < 1:
				print("Guess is small...")
			elif prediction < 0.5 and prediction > 0:
				print("Guess is too small...")
			print("Try Again...")
	else:
		return entry_fees * -1
		
	
def stop_game(prize):
	if prize > 0:
		print("You win ",prize)
	else:
		print("Loss")

def guess_the_number():
	sn, rewards, entry_fees = initialization()
	prize = start_game(sn, rewards, entry_fees)
	stop_game(prize)
	
guess_the_number()
