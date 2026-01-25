phone=dict()
i=1
n=int(input("Enter number of enteries:"))
while i<=n:
    a=input("Enter Name:")
    b=input("Enter phone no:")
    phone[a]=b
    i=i+1
l=phone.keys()
x=int(input("Enter the name to be searched:"))
for i in l:
    if i==x:
        print(x,": phone no =",phone[i])
        break
    else:
        print(x,"not exist......")