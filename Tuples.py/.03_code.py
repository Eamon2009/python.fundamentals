# This code input a Tuple
# Find maximum number
# Find minimum number
# Find sum of all Elements
# Find mean value
t1=tuple()
n=int(input("Enter the number of element:"))
for i in range(0,n):
    i=int(input("--"))
    t1=t1+(i,)
print(t1)
print("The maximum number is:")
print(max(t1))
print("The minimum number is:")
print(min(t1))
print("The sum of all Elements:")
print(sum(t1))
mean=sum(t1)/len(t1)
print("The mean value of Tuple is:")
print(mean)