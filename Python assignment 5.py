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