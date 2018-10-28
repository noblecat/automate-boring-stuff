spam = ['koty','myszy','konie']

def iplus(arg):
	if len(arg) > 1:
		for i in range(len(arg)-2):
			print((str(arg[i])) + ", ", end="")
		print((str(arg[-2]) + ' i ' + str(arg[-1])))
	elif len(arg) == 1:
		print(arg[0])
	else:
		print('*** empty list ***')

iplus(spam)