# This code take n number of country it's currency and capital 
# Display in Tabular Form 
di=dict()
i=1
n=int(input("Enter number of entries:"))
while i<=n:
    c=input("Enter the country:")
    cap=input("Enter the Capital:")
    curr=input("Enter the currency of country:")
    di[c]=(cap,curr)
    i=i+1
l=di.keys()
print("\nCountry\t\t","capital\t\t","currency")
for i in l:
    z=di[i]
    print('\n',i,'\t\t',end='')
    for j in z:
        print(j,'\t\t',end="\t\t")
x=input("\nEnter Country:")
for i in l:
    if i==x:
        print("\nCountry\t\t","Capital\t\t","Currency\t\t")
        z=di[i]
        print('\n',i,"\t\t",end="")
        for j in z:
            print(j,"\t\t",end="\t\t")
        break