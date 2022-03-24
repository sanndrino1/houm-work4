#numbers=[]
#x=int(input('enter a number [0 for end]:'))
#while x !=0:
    #numbers.append(x)
    #x= int(input('entar a number[0 for end] :'))#sorted_numbers = sorted(numbers)
    #sorted_numbers=sorted(numbers)
#for num in sorted_numbers:
    #print(num)
    
    # 2. При анализиране на данни, събрани като част от научен експеримент, може
#да се наложи да се премахнат най-крайните (големите) стойности, преди да се
#извършват някакви други изчисления. Да се създаде списък от стойностите само с n на
#брой положителни числа.
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
      

    
try:
    number  = [1,2,14,6,30,4,50,9,7,80,90]
    number=int(input('enter a number [ for end]:'))
except:
    sorted_number=sorted(number)
    print(number)
    sorted_number=sorted(number)
    print(sorted_number)
    print((sorted_number[-2:]))
    sorted_number_one=sorted(number)
    print(sorted_number_one)
    print((sorted_number_one[:2]))
    
numbers=[]

x=int(input('enter a number [0 for end]:'))
while x !=0  :
    numbers.append(x)
    x= int(input('entar a number[0 for end] :'))#sorted_numbers = sorted(numbers)
    sorted_numbers=sorted(numbers)
    
for num in sorted_numbers:
    print(num)

  


   