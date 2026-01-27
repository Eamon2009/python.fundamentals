#This is a basic code to understand function in python
#This code find out greatest of three numbers
def greatest(a,b,c):
       #a=int(input(">"))
       #b=int(input(">>"))
       #c=int(input(">>>"))
       if a>=b and a>=c :
              print(f"{a} is greatest integer")
       elif b>=c and b>=a :
              print(f"{b} is the greatest integer")
       else:
              
              print(f"{c} is the greatest integer")
greatest(1,23,45)