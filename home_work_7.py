numbers=[]
rayn=[]
x=0
y=0
while True:
    x=str(input("enter city:"))
    
    if x =='':
        break
    y=int(input("enter rayn in mm:"))
    numbers.append(x)
number_new=sorted(numbers)
for  el in number_new:
    rayn.append(y)
    rayns_new=sorted(rayn)
for  al in rayns_new:
    
    print("city:{}!".format(el))
    print("rayn in mm:{}!" .format(al))
