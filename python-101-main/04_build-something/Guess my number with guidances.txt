import random

num = random.randint(1,10)
guess = None

while guess!=num:
	guess = input ("guess a number between 1 and 10: ")
	guess = int(guess)
	if guess  == num:
		print ("Congratulations!")
		break
	else:
		print ("No, sorry try again")
		if guess > num:
			print("Your guess is higuer than the number, try a lower number! ")
		if guess < num:
			print("Your guess is lower than the number, try a higuer number! ")