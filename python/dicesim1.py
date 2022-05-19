import random

while True:
	print('''Naciśnij 1, aby rzucić kością. Naciśnij 2, aby zakończyć. ''')
	user = int(input("Twój wybór: \n"))
	if user==1:
		number = random.randint(1,6)
		print(number)
	else:
		break
