#1.zada4a 
#for num in range(1500, 2700):
    #if num %7==0 and num% 5==0:
       # print(num)
#2.zada4a
#1 wariantprint(sum(range(1,11)))
#2  variant
#curent = 0
#for num in range(1,11):
    #curent += num
#print(curent)

#width = 10
#for i in range(1,width+1):
       # print('*'*i)
#for j in range(width-1,0,-1):
                #print('*'*j)

       #5 zada4a   

#word = 'hello'
# 1 wi Metod
#for char in range(len(word) - 1, -1, -1):
  #print(word[char], end="")
#print("\n")

#2-ri Metod
##word='Hello'
#i = 0
#while i < len(word):
    #print (word[i-1])
    #i -= 1

  #Задача 5. Да се напише програма, която да намира броят на четните и нечетните числа
#от списък от цели числа.

#numbers= [1,2,3,4,5,6,7,8,9]
#even_count, odd_count = 0, 0
#i= 0
#while(i < len(numbers)):
    
    #if numbers[i] % 2 == 0:
       # even_count += 1
    #else:
       # odd_count += 1
    #i += 1
      
#print("Even numbers : " ,even_count)
#print("Odd numbers : ", odd_count)

#Задача 6. Да се напише програма, която да принтира всички числа от 0 до 6, без да
#включва 3 и 6.

for num in range(0, 6):
    if num==3:
       continue
    if num==6:
        continue
    print(num)
    