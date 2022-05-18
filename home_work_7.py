

#Проектът представлява обикновена банкова система. Той съдържа само
#административна част, без да се дава възможност на потребителя да влиза в система с
#потребителско име и парола. Административната част включва всички основни
#функции: създаване на нов акаунт, преглед на записа на притежателите на акаунти,
#теглене и депозит на сума, запитване за салдо. Потребителят трябва лесно да може да
#проверява общите записи на банковата сметка. Потребителят може да създаде акаунт,
##като предостави първоначална сума за депозиране. Той може да депозира и тегли пари
#само като предостави номера на потребителската си сметка и въведе сума.
#Потребителят може да проверява за клиенти и техният баланс по сметка. 











user=[]
user_All_Holders=[]
  
user_Account = [
    'id',
 	'name',
    'deposit',
    'balance',
 	'withdrawl',
     'Customer_Card',
     'pin'
]

id=input('Enter ID:')

if  id.isdigit():
    print("Pin!: Wellcome:!")
else:
    print("Pin is  not a digit!")


if len(id) == 10:
        print(" Your ID !:",id) 
else:
        print("False Pin: Enter a Valid ID Cod Please !:") 

 
name=input('Enter Name:')

for char in name:
    if((char>='a' and char<= 'z') or (char>='A' and char<='Z')):
        print(char, "is an Alphabet")
    else:
        print(char, "is not an Alphabet")
        
        print('Yuor Name:',name)
       
    
balance=2000
deposit=float(input("Enter the amount to be deposit: "))
balance = balance + deposit
print ("The deposit is successful and the balance in the account is ",balance)
withdrawl=float(input("Enter the amount to withdraw: "))
if (balance >= withdrawl):

    balance = balance - withdrawl
    print ("The withdraw is successful and the balance is " ,balance)
else:
    print ('Insuficient Balance')
card_Holder=input('Enter Card:')
for char in card_Holder:
    if len(str(card_Holder)) > 4 or len(int(card_Holder)) >12:
        if  not (("A" <= char and char <= "Z")  or (char == " ")):
            print("INVALID CARD !:")
            break
        else:
            print("VALID CARD ")
Pin=input('Enter Pin:')

if  Pin.isdigit():
    print("Pin!: Wellcome:!")
else:
    print("Pin is  not a digit!")

if len(Pin) == 4:
    print(" Your Pin !:",Pin) 
else:
    print("False Pin: Enter a Valid Pin Cod Please !:") 

user_Account= [id,name, deposit,balance,withdrawl,card_Holder,Pin]
if user_Account  and id and name and balance and deposit and withdrawl and card_Holder  and Pin in user_Account:
   print ("That user already exsist",user_Account)
user.append(user_Account)
print(user)

i=0                        
option=int(input('enter Option:'))    
for  i in range(0,option):
                  
    if option==1:
        print('Holders Account:',user_Account)
        break
    if option==2:
        print('Create New Account:')
                                              
                             
while True:

    word=input('Enter Q for Create New Account: ' )
    id=input('Enter ID:')
    if  id.isdigit():
        print("Pin!: Wellcome:!")
    else:
        print("Pin is  not a digit!")

    if len(id) == 10:
        print(" Your Pin !:",id) 
    else:
        print("False Pin: Enter a Valid Pin Cod Please !:") 
 
    name=input('Enter Name:')
    for char in name:
        if((char>='a' and char<= 'z') or (char>='A' and char<='Z')):
            print(char, "is an Alphabet")
        else:
            print(char, "is not an Alphabet")
        
            print('Yuor Name:',name)
    
        balance=2000
        deposit=float(input("Enter the amount to be deposit: "))
        balance = balance + deposit
        print ("The deposit is successful and the balance in the account is ",balance)
        withdrawl=float(input("Enter the amount to withdraw: "))
        if (balance >= withdrawl):
            balance = balance - withdrawl
            print ("The withdraw is successful and the balance is " ,balance)
        else:
            print ('Insuficient Balance')
    card_Holder=input('Enter Card:')
    for char in card_Holder:
        if len(str(card_Holder)) > 4 or len(int(card_Holder)) >12:
            if  not (("A" <= char and char <= "Z")  or (char == " ")):
                print("INVALID CARD !:")
                break
            else:
                print("VALID CARD ")
    Pin=input('Enter Pin:')
    if  Pin.isdigit():
        print("Pin!: Wellcome:!")
    else:
        print("Pin is  not a digit!")

        if len(Pin) == 4:
            print(" Your Pin !:",Pin) 
        else:
            print("False Pin: Enter a Valid Pin Cod Please !:")

        if id==0:
            break

    user.append([word,id,name, deposit,balance,withdrawl,card_Holder,Pin])
    print(user)
    user = [word,id,name, deposit,balance,withdrawl,card_Holder,Pin]

    user_All_Holders.append(user)
    print(user_All_Holders)
    break
        
       

n = int(input('Please enter the Holders of iterations:\n'))
i=0

for i in range(0,n):
   
        
    name = input("Give name:")
    if id == id:
    
        print("ID inputs are correct!")
        continue
    else:
        print("The given ID is incorrect.")
        break

        
        
             
    if i ==0:
            print('Enter 0 for choice 0 for Add  New Holder   \n')
            print('Enter 1 for choice 1 for Holder Withdrawl: \n Enter 2 for choice 2 for Holder Withdrawl: \n,Enter 3 for choice Holder Balance:\n')
    for i in range(0,n):
        if i ==0:
            if i  ==1:
                print('Enter 1 for choice 1 Deposit :\n')
    if i  ==2:
        print('Enter 2 for choice 2 for Holder Withdrawl: \n')
    if i ==3:
        print('Enter 3 for choice Holder Balance:\n')

    choice = int(input('Enter your choice:'))
    if (choice==0):
     print('Account Number:',user)
    choice = int(input('Enter your choice:'))
    
    if (choice == 1):
        print('Holder Deposit:',deposit)
        print( ' Holders Deposit:\n If  Holders wont more Deposit Please pres 2')
        deposit=float(input("Enter the amount to be deposit: "))
        balance = balance + deposit
        print ("The deposit is successful and the balance in the account is ",balance)

    if (choice == 2):
        print('Holder Withdrawl:',withdrawl)  
        withdrawl=float(input("Enter the amount to withdraw: "))
        print(withdrawl)
    if (int(balance) >= float(withdrawl)):
            balance = int(balance) - float(withdrawl)
            print('Enter Withdrawl',withdrawl)
            print ("The withdraw is successful and the balance is " ,balance)

    else:
            print ('Insuficient Balance')  
    if (choice == 3):
        print('Holder Balance:',balance)
    if (choice == 4):
        print(' All Bank Holders:', name)
    
    else:
        print('Invalid choice:')
           
            


