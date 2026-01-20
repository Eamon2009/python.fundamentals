#This program does following:
#Number of uppercase letters
#Number of lowercase letters
#Number of alphabets
#Number of digits
line=input("Enter a line:")
lower=upper=0
digi=alpha=0
for i in line:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1
    elif i.isdigit():
        digi+=1
    elif i.isalpha():
        alpha+=1
print(f"Number of uppercase letters:{upper}")
print(f"Number of lowercase letters:{lower}")
print(f"Number of alphabets:{alpha}")
print(f"Number of digits:{digi}")
