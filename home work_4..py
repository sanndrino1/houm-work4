
# ..........Задача 1. Да се напише if-конструкция, която проверява стойността на две целочислени
#променливи и разменя техните стойности, ако стойността на първата променлива е по-голяма
# от втората....... 

a = 10
b = 6
if   b > a :
    
    
    
    print("b is greater than a")
elif a == b:
            print("a and b are equal")

else:
        print("a is greater than b")
    



#Zada4a 2.Напишете програма, която показва знака (+ или -) от частното на две реални числа,
без да го пресмята. 

x=10
y=-10
if x>0  :
    print('+')
if y<0:
    print('-')
#.............................................................
#Задача 3. Напишете програма, която намира най-голямото по стойност число, измежду три
#дадени числа. ..........................................
num1 = 1
num2 = 2
num3 = 3
 
if (num1 > num2) and (num1 > num3):
   print(largest = num1)
elif (num2 > num1) and (num2 > num3):
   print(largest = num2)
else:
   largest = num3
 
print("The largest number is",largest)

#Задача 4. Напишете програма, която за дадена цифра (0-9), зададена като вход, извежда името
#на цифрата на български език. 
#
s=0
a=1
b=2
c=3
d=4
e=5
f=6
j=7
h=8
k=9
if s==0:
    print('nula')
if a==1:
    print('edno')
if b==2:
    print('dve')
if c==3:
    print('tri')
if d==4:
    print('4etry')
if e==5:
    print('pet')
if f==6:
    print('6est')
if j==7:
    print('sedem')
if h==8:
    print('osem')
if k==9:
    print('devet')

# Задача 5. Напишете програма, която при въвеждане на коефициентите (a, b и c) на квадратно
уравнение ax^2+bx+c изчислява и извежда неговите реални корени. 

import cmath
a=5
b=10
c=10
d=(b**2) - (4*a*c)



if a== 0:
        print('УРАВНЕНИЕТО НЯМА РЕШЕНИЕ')
if d <0:
        print('уравнението няма реални корени ')
       
elif d==(b**2) - (4*a*c):
    print(d)
   

a=5
b=10
c=-15
d=(b**2) - (4*a*c)
x =- b/(2*a)
x1=(-b-cmath.sqrt(d))/(2*a)
x2=(-b+cmath.sqrt(d))/(2*a)


if a== 0:
        print('УРАВНЕНИЕТО НЯМА kvadratno')
if d==0:
    print ('stop')
elif(x==- b/(2*a)):
    print(x)
if d < 0:
        print( 'noting')

elif d==(b**2) - (4*a*c):
    print(d)
if(x1==(-b-cmath.sqrt(d))/(2*a)):
    print(x1)
if(x2==(-b+cmath.sqrt(d))/(2*a)):
    print(x2)
    print('The solution are {0} and {1}'.format(x1,x2))
