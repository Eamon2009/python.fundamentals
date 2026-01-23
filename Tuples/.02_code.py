# This code input 2 tuples and swap their value
t=tuple()
n=int(input("Enter the no.of element you want:"))
for i in range(n):
    i =int(input("Enter the element:"))
    t=t+(i,)
t2=tuple()
n=int(input("Enter the no.of element you want:"))
for a in range(n):
    a =int(input("Enter the element:"))
    t2=t2+(a,)
print("First Tuple:")
print(t)
print("Second Tuple:")
print(t2)
t,t2=t2,t
print("Swaped tuple1:")
print(t)
print("Swaped tuple2")
print(t2)

