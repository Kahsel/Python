def evenOdd(*args):
    evenList = [n for n in args if n%2==0]
    oddList = [n for n in args if n%2==1]
    return f'EvenList: {evenList}\nOddNumber: {oddList}'

output = evenOdd(1,2,3,4,5,6,7,8,9,10)
print(output)