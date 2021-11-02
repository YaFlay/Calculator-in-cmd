# https://github.com/yaflay
import time
# take modules

number_1 = int(input('First number = ') )
time.sleep(0.3)
# take first number

number_2 = int(input('Second number = ') )
time.sleep(0.3)
#  take second number

operator = input('Operator = ')
time.sleep(0.3)
# take operator

a = str(number_1) + str(operator) + str(number_2)+ '='
print(a)

if operator == '/':
   print(number_1 / number_2)
#  calculation
else: 
        if operator == '-':
                print(number_1 - number_2)
        else:
                if operator == '*':
                        print(number_1 * number_2)
                else: 
                        if operator == '+':
                            print(number_1 + number_2)
                        else:
                                    if operator == '%':
                                            print(number_1 % number_2)
                                    else:
                                            if operator == '**':
                                                    print(number_1 ** number_2)

# Hello, this is my first work on GitHub. Thanks for some attention
