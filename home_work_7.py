from collections import UserList
from tokenize import Name

#Проект 5 Управление на банкова сметка
#Описание:
#Проектът представлява обикновена банкова система. Той съдържа само
#административна част, без да се дава възможност на потребителя да влиза в система с
#потребителско име и парола. Административната част включва всички основни
#функции: създаване на нов акаунт, преглед на записа на притежателите на акаунти,
#теглене и депозит на сума, запитване за салдо. Потребителят трябва лесно да може да
#проверява общите записи на банковата сметка. Потребителят може да създаде акаунт,
#като предостави първоначална сума за депозиране. Той може да депозира и тегли пари
#само като предостави номера на потребителската си сметка и въведе сума.
#Потребителят може да проверява за клиенти и техният баланс по сметка.





list_B=[]

Number=0
withdrawl=0
balance = 2000
deposit=0
FarstName=''
LastName=''
list_A=[
'Open You Account::'
'Number Account:',
'Name:!',
'Withdrawl1:',
'Deposit1:',
' Check_Balance:',
'Membar Account'

'Exit']


print('Oppen You New Account :!  Enter 1:!')
option = int(input('Choose an Option:'))

if option==1:
  try:
    Number=int(input('Enter Your Number Account {}:!!!'))
  except:
    for x in Number():
                if (Number == " "):
                    if 0 < len(Number)>=2:
                        print('False Numer')
                    else:
                      Number=Number
                      print('Number is:',Number)
  print('Member Account Number  ''{} :!!!'.format(Number))
  FarstName=input('Farst Name:!!')
  if  len(FarstName)>20:
      print('False Name:!')
  else:
    print(FarstName.upper())
  LastName=input('Last Name:!!')
  if len(LastName)>20:
      print('False Last Name:!')   
  else:
      print(LastName.upper())
      for char in Name:
          if  not (("A"<= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
               print('FALSE Entering Name:...')
          else:
              print('Yuor Name:',Name.upper())
    
  print('Full Name {}:!!'.format(FarstName + '  ' + LastName))
  withdrawl += float(input('How much do you want to Withdrawl?:'))
  balance = balance - withdrawl
  print (' New Balance {} :!'.format (balance))
  if   withdrawl >balance:
    print(' Withdraw  is Biggest then Balance :!!!')
    print('stop {}:!!'.format(quit()))
  deposit = int(input('How much do you want to Deposit?:'))
  balance = balance + deposit
  print (   ' New Balance:', balance)
  print(  'Balance:',        balance)
  balance -= withdrawl
  print('current_balance '  '{}:!! '.format(balance))

  print('....................................')
  print('........Total Acount:!..............')
  print('Acount Number:  {}   :!' .format(Number))
  print('Full Name:      {}   :!'.format(FarstName +  '  '  + LastName))
  print('Balance:        {}   :!'.format(balance))
  print('Withdrawl:      {}   :!'.format(withdrawl))
  print('Deposit:        {}   :!'.format(deposit))
  print('...................................')
  print(36*'*')
  print('.............Customer Date...........' ) 

list_B=list_A.append(option)

option = int(input('Choose an Option:'))
for x in list_A:
  if option==2:
    print(' Full Name  :! {}'.format(FarstName) + '  ' + ':! {} ' .format(LastName))
    print(50*'*')
    #print('Full Name {}:!!'.format(Name))
    option = int(input('Choose an Option:'))

  if option == 3:
    print(' WITHDRAWL :! {} '.format(withdrawl))
    withdrawl += float(input('How much do you want to Withdrawl?:'))
    print(20*'*')
    print('Withdrawl :! {} '.format(withdrawl))
    balance = balance - withdrawl
    print(20*'*')
    print('New Withdrawl  {} :!'.format(withdrawl))
    print (' New Balance  {} :!'.format (balance))
    option = int(input('Choose an Option:'))
       
  elif option == 4:
    print('Deposit  :! {} '.format(deposit))
    deposit = int(input('How much do you want to Deposit?:'))
    print(20*'*')
    print(' New Deposit :! {} '.format(deposit))
    
    print(20*'*')
    #print('Deposit {}:!'.format(deposit) )
    balance = balance + deposit
    print(20*'*')
    print (' New Balance:', balance)
    print(20*'*')
    option = int(input('Choose an Option:'))
  elif option == 5:
    print('.................')
    print()
    print('Balance:', balance)
    print('..................')
    balance -= withdrawl
    print(30*'*')
    print('current_balance '  ':!! ',balance)
    print(30*'*')
    print (' Thank you for using THE STEVENS UNIVERSAL BANK ')
    option = int(input('Choose an Option:'))
  if option == 6:
    print('Account Number  :! {}'.format(Number))
    print('Account Number :! {}'.format(Number) +'  '+'Account Name:! {}'.format(FarstName) +' '+'{}'.format(LastName))
    option = int(input('Choose an Option:'))
    print('Account Number :! {}'.format(Number) +'  '+'Account Name:! {}'.format(FarstName) +' '+'{}'.format(LastName))
  if option == 7:
    print('Account Membar  :!' 'Acount Number :!'',', Number ,',','Full Name: {} '.format(FarstName) + '  ' + ' {} ' .format(LastName)  , ',' 'WITHDRAWL {}:!'.format(withdrawl),'DEPOSIT {} :!'.format(deposit),'Balnce {}:!'.format(balance))
    print (' Thank you for using THE  UNICCREDIT BANK ')
    exit()
    
    