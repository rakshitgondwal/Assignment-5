
#Question1
print("\nWelcome to my Program")
char = str(input("Kindly enter a string : "))
print("\nThe string in reverse order : ")
print(char[::-1])


#Question2
print("\nWelcome to my Program")
lrange = int(input("Kindly enter the lower limit of the divisibility range : "))
uprange = int(input("Kindly enter the upper limit of the divisibility range : "))
thenum = int(input("Kindly enter the number that is to be divided : "))
print("\nNumbers divisible in the given range are as follows : ")
for i in range(lrange , uprange + 1):
   if(i%thenum==0):
      print(i)
        
        
#Question3        
print("\nWelcome to my Program")
import math
a = int(input("Please enter the length of side 1 : "))
b = int(input("Please enter the length of side 2 : "))
c = int(input("Please enter the length of side 3 : "))
while ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    s = (a + b + c) / 2
    Area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("\nArea of the triangle is : ",Area)
    break
while ((a+b)<c) or ((a+c)<b) or ((b+c)<a):
    print("\nThe combination of the sides entered isn't possible !")
    break        
    
    
    
#Question4    
print("\nWelcome to my Program")
n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
    
    
    
    
    
    
#Question5    
print("\nWelcome to my Program")
asciichr = 65
num = int(input("Kindly enter the number of rows : "))
for i in range(0,num):
    for j in range(0,i+1):
        if asciichr > 90:
            asciichr = 65
        char = chr(asciichr)
        print(char,end="")
        asciichr += 1
    print()
    
    
    
    
    
    
#Question6    
print("\nWelcome to my Program")
print()
lrange = int(input("Kindly enter the lower limit : "))
uprange = int(input("Kindly enter the upper limit : "))

print("\nPrime numbers between", lrange, "and", uprange, "are : ")

for num in range(lrange, uprange + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
            
            
            
            
            
            
#Question7            
 print("\nWelcome to my Program")
print("\nBetween 1 and 500 the following numbers are multiple of 7 : ")
for i in range(1,501) :
    if i%7 == 0 :
        print(i)
print("\nBetween 1 and 500 the following numbers are divisible by 11 : ")
for i in range(1,501) :
    if i%11 == 0 :
        print(i)
print("\nBetween 1 and 500 the following numbers are both multiple of 7 and divisible by 11 : ")
for i in range(1,501) :
    if i%7 == 0 and i%11 == 0 :
        print(i)
        
        
        
        
        
        
#Question8        
print("\nWelcome to my Program")
postivenum=[]
negativenum=[]
oddnum=[]
evennum=[]
occurrence={}
list=[]
for i in range(10):
    num=int(input("Kindly enter the number : "))
    list.append(num)
    if num>=0:
        postivenum.append(num)
    elif num<0 :
        negativenum.append(num)
    if num%2==0 :
        evennum.append(num)
    elif num%2!=0 :
        oddnum.append(num)
    if num not in occurrence :
            occurrence[num]=1
    elif num in occurrence :
        occurrence[num]+=1
print("Positive Numbers : ",postivenum)
print("Negative Numbers : ",negativenum)
print("Even Numbers : ",evennum)
print("Odd Numbers : ",oddnum)
print("Occurrence of each number in the List : ",occurrence)






#Question9
print("\nWelcome to my Program")
list = []
ele = str(input("\nKindly enter a string : "))
list = ele.split(" ")
occurrence = {}
for i in list :
    if i not in occurrence :
        occurrence[i]=1
    else :
        occurrence[i]+=1
print("\nNumber of occurrences of each word is : ",occurrence)
