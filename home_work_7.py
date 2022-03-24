#Задача 1. Напишете програма, която чете цели числа въведени от потребителя и ги
##съхранява в списък. Програма трябва да продължи да чете стойности, докато
#потребителят не въведе 0. След това тя трябва да покаже всички стойности, въведени от
##потребителя (с изключение на 0), подредени от най-малката до най-голямата стойност,
#като на всеки ред се появява по една стойност. Използвайте или метода за сортиране,
#или функцията за сортиране на списъци.






#numbers=[]
#x=int(input('enter a number [0 for end]:'))
#while x !=0:
    #numbers.append(x)
    #x= int(input('entar a number[0 for end] :'))#sorted_numbers = sorted(numbers)
    #sorted_numbers=sorted(numbers)
#for num in sorted_numbers:
    #print(num)
    
    # Лекция 7 Списъци

#Задача 2. При анализиране на данни, събрани като част от научен експеримент, може
#да се наложи да се премахнат най-крайните (големите) стойности, преди да се
##извършват някакви други изчисления. Да се създаде списък от стойностите само с n на
#брой положителни числа. Трябва да се създаде ново копие на създаденият списък с
##премахнатите n най-големи елемента и n най-малките елементи. Редът на елементите
#във върнатия списък не трябва да съвпада с реда на елементите в първоначалния
#списък. Напишете програма, която да чете списък от числа въведени от потребителя и
#да премахва двете най-големи и двете най-малки стойности. Да се принтира новият
##списък, както и оригиналният. Програма трябва да генерира подходящо съобщение за
#грешка, ако потребителят въведе по-малко от 4 стойности.

##even=0
#odd=0
##set = [12,13,-14,15,-16,17,18,19,20]


#print(min(set))
#print(max(set))
#set_copy=set[:]
#print(set_copy)
#removed_set = set.pop()
#print(removed_set)
#print(set)
#for num in set:
    #if num >= 0:
      # even += 1
    #else:
        ##odd += 1
#print( even)
#print( odd)
#for even in set:
    #if even > 0:
       # print(even, end = " ")







   #     l = [1000,298,3579,100,200,-45,900]
    #n = 2
  
    #l.sort()
    #print(l[-n:])

    #new_set_copy=(set)
    #new_set_copy.remove(max(new_set_copy))
    #print(max(new_set_copy))
    #one_set_copy=(set)
    #one_set_copy.remove(min(one_set_copy))
    #print(min(one_set_copy))
      

    
#try:
    #number  = [1,2,14,6,30,4,50,9,7,80,90]
    #number=int(input('enter a number [ for end]:'))
#except:
    #sorted_number=sorted(number)
    #print(number)
    #sorted_number=sorted(number)
    #print(sorted_number)
    #print((sorted_number[-2:]))
    #sorted_number_one=sorted(number)
    #print(sorted_number_one)
    #print((sorted_number_one[:2]))
    
num = (input('Enter the 4 digit number[]'))
num_length = int (len(num))
try :
    
    if (num_length == 4) :
        
        num = int (num)
        
        i = 1
        even_count = 0
        odd_count = 0
        zero_count = 0
      
        while (i <= num_length) :
           
            digit = int (num % 10)
            if (digit == 0) :
                zero_count +=1
            elif (digit %2 == 0) :
                even_count +=1
            else :
                odd_count +=1
            i += 1
            num /= 10
            
        print (f"Count of even numbers: {even_count}\n")
        print (f"Count of odd numbers: {odd_count}\n")
        print (f"Count of zero numbers: {zero_count}\n")

    else :
        print ("Please enter 4 digit number only")

except ValueError:
    print("Please enter valid 4 digit number only! (No decimals or strings allowed please!)")
    