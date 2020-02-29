import math
print("enter 1st number")
number = int(input())
print("enter 2nd number")
number2 = int(input())
print('what u want?'+'*,/,%,+,-')
number3 = input()
if number == 45 and number2 == 3 and number3 == '*' :
 print("555")
elif number == 56 and number2 ==6 and number3 == '/':
 print("77")
elif number == 56 and number2 ==9 and number3 == '+':
 print("4")
elif number3=='*':
 multi=number*number2
 print(multi)
elif number3=='+':
 plus=number+number2
 print(plus)

elif  number3=='-' :
 minus=number-number2
 print(minus)
elif number3=='/':
 div=number/number2
 print(div)
elif number3=='%':
 percent=number%number2
 print(percent)
