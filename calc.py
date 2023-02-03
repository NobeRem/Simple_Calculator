def division(x,y):
	return x / y 

def subtract(x,y):
	return x - y  

def multiply(x,y):
	return x * y 

def add(x,y):
	return x + y


print('addition: 1')
print('subtraction: 2')
print('multiplication: 3')
print('division: 4')

while True:
	choice = int(input('Select Operation #: '))

	if choice in range(1,4):
		try:
			num1 = int(input('# operating by: '))
			num2 = int(input('# operating by: '))
		except ValueError:
			print('Wrong input, Input a number')
			continue 

	if choice == 1:
		print(num1,'+',num2,'=', add(num1, num2))

	elif choice == 2:
		print(num1,'-',num2,'=', subtract(num1, num2))

	elif choice == 3:
		print(num1,'*',num2,'=', multiply(num1, num2))

	elif choice == 4:
		print(num1,'+',num2,'=', division(num1, num2))

	cont = input('Do you wish to continue?: (y/n)')
	if cont == 'y':
		continue  
	else:
		break 
