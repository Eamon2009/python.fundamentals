#This code perform a linear search in Tuple
tu=(1,2,3,4,5,6)
n=int(input("Enter the element to be searched:"))
fd=False
for i in range(len(tu)):
    if tu[i]==n:
        print("Element found at index",n)
        fd=True
if fd==True:
    print("SUCCESSFUL search")
else:
    print("Not Found")
    



