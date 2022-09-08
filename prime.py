<<<<<<< HEAD
class primeNums:
    
    def isPrime():
        print('Welcome to Prime Identification of Numbers')
        num = ''
        num = int(input('Pls! Enter Number: '))
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num%i)==0:
                    return f'Sir/Ma {num} is not a Prime Number'
                    break
            else:
                return f'Sir/Ma {num} is a Prime Number'
        else:
            return f'Sir/Ma {num} is not a Prime Number'
    
print(primeNums.isPrime())
=======
class isPrime:
    def primeNumbers():
        print('Welcome to the Prime Numbers world!')
        inputValue = ''
        inputValue = int(input('Comrade! Enter Nnumber: '))
        if inputValue > 1:
            for i in range(2, int(inputValue/2)+1):
                if (inputValue%i) == 0:
                    return f'The number {inputValue} is not a Prime Number'
                    #break
            else:
                return f'The number {inputValue} is a Prime Number'
        else:
            return f'The number {inputValue} is not a Prime Number'
        
result = isPrime.primeNumbers()
print(result)
>>>>>>> 9e40ca1 (succesfully)
