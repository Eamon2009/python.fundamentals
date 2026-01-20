#Program that read a string and then
#print the string that capitalises every other letter in the string
st=input("Enter a string:")
length=len(st)
print(f"Original String:{st}")
st2=""
for i in range(0,length,2):
    st2+=st[i]
    if i<length-1:
        st2+=st[i+1].upper()
print("Alternatively capatilized string:",st2)