n=int(input("How many nos. in the list? :"))
list=[]
print("Enter the nos.")
for i in range(0,n):
    list.append(int(input()))
num=int(input("Which no. you want to search ?:"))
if num in list:
    print(True)
else :
    print(False)
        
