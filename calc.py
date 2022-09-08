def calculate():
    operation = input(''' 
                    Please input the operator you will be using:
                    + for additon
                    - for subtraction
                    * for multiplication
                    / for division
                    ** for raise power
                    % for modulo
                    ''')

    num1 = int(input('Enter first Number: '))
    num2 = int(input('Enter second Number: '))

    #addition
    if operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)
    #substraction
    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)
    #multiplicaton
    elif operation == '*':
        print('{} x {} = '.format(num1, num2))
        print(num1 * num2)
    #division
    elif operation == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1/num2 if num2!=0 else 0)
    #for raise power
    elif operation == '**':
        print('{} ^ {} = '.format(num1, num2))
        print(num1 ** num2)
    #for remainder
    elif operation == '%':
        print('{} % {} = '.format(num1, num2))
        print(num1 % num2 if num2!=0 else 0)
    #collection of error
    else:
        print('You have not type a valid operator, please run the program again and type a valid operator!')
    
    again()
    
 #for calculating calculation again
def again():
    calc_again = input(''' Do you want to calculate again?!
    enter y for yes and n for no.
    ''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you sometime')
    else:
        again()
        
calculate()