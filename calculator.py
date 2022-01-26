def add(num1, num2):
    return(num1 + num2)
def subtract(num1, num2):
    return(num1 - num2)
def multiply(num1, num2):
    return(num1 * num2)
def divide(num1, num2):
    return(num1 / num2)

i = 1

while i >= 1 :
    print('Operations: \n' 
      '1. Addition \n' 
      '2. Subtraction \n' 
      '3. Multiplication \n' 
      '4. Division')
    choice = int(input('Select an operation: '))
    while choice<=0 or choice>4:
        print('Invalid Operation. \n' 
              'Operations: \n' 
              '1. Addition \n' 
              '2. Subtraction \n' 
              '3. Multiplication \n' 
              '4. Division')
        choice = int(input('Select a valid operation: '))
    num1 = int(input('Choose first number: '))
    num2 = int(input('Choose second number: '))

    if choice == 1:
        print(num1, ' + ', num2, " = ", add(num1, num2))
    elif choice == 2:
        print(num1, ' - ', num2, " = ", subtract(num1, num2))
    elif choice == 3:
        print(num1, ' * ', num2, " = ", multiply(num1, num2))
    elif choice == 4:
        while num2 == 0:
            num2 = int(input('Choose second number, other than 0: '))
        print(num1, ' / ', num2, " = ", divide(num1, num2))
    else:
        print('Invalid Input.')
    string = input('Do another calculation? Y/N: ')
    while string != 'N' and string != 'Y':
        string = input('Do another calculation? Please enter valid answer with Y/N: ')
    if string == 'Y':
        i = 1
    elif string == 'N':
        i = 0









