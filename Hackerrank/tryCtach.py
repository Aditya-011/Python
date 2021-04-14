# example of unpredictable
# behaviour of int()
try:
    num1 = float(input(''))
    num2 = float(input(''))
    num1 = int(num1)
    num2 = int(num2)
    #print(num1, num2, sep = '\n')
except ValueError:
    print('Please type an integer')
