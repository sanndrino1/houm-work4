#  Задача 3. Да се създаде речник, който да съдържа информацията за дадено меню на
#ресторант. Ключовете му трябва да са стрингове, а стойностите цените. Програмата ще
#поиска от потребителя да въведе следната информация:
#Ако потребителят въведе името на дадено ястие от менюто, тогава програмата
#да принтира цената и колко е общата цена до момента. След това да пита
#отново дали потребителят не иска да въведе нещо друго.
#Ако потребителят въведе име на ястие, което не е в менюто, тогава програмата
#да изведе подходящо съобщение. След което отново програмата да пита
#потребителя да избере нещо друго от менюто.
#Ако потребителят въведе празен стринг, тогава програмата да спре да подканва
#потребителя да избира от менюто и да изведе на екрана общата крайна сума.



import keyword
from multiprocessing.sharedctypes import Value
from optparse import Values
from tkinter import Menu
from typing import KeysView

menu=[]
lst = []
total=0
sum=0
h=0
fi=0

d={'salat':5,'filet':10}

while True :
    try:
        x=str(input('Choice menu:'))
    except:
  
        if x=='':
            break
    if x not in d:
       print("choise food")
       continue
    
      
        
    
    if 'salat' in x:
        
        print(d['salat'],'lv')
        
        if 'filet' in x:
        
            print(d['filet'],'lv')
        
        
        
        
        
    
        
    
    
    
    
    menu.append(x)
       
    menu_new = sorted(menu)
    
    for l in menu_new:
       

        for l in range(0, len(menu_new)):
            l += 1
            sum = 0
            sum = sum + l
            sum1=5
            sum2=10
            sum3=total
            h  = menu_new.count('salat')
            fi = menu_new.count('filet')
            total=(sum1*h+sum2*fi)
            print(f'{h} salat //:::: //{fi} filet')
            print("Count of food ", menu_new, "price is : ", sum)
            
            
            print(total)
            print(f'TOTAL: - {total}')
            
            
            
            
               

            
               
            
                
                
            
