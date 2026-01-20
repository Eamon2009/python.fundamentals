# this program accept a string and display the longest sub-string
#Just having the consonaents.
st=input("Enter a String:")
length=len(st)
maxlength=0
maxsub=''
sub=""
lensub=0
for i in range(length):
    if st[i] in 'aeiou'or st[i] in "AEIOU":
        if lensub>maxlength:
            maxsub=sub
            maxlength=lensub
            sub=""
            lensub=0
        else:
            sub+=st[i]
            lensub=len(sub)
            a+=1
print("Maximum length consonant substring is:",maxsub,end=" ")
print("with",maxlength,"characters")
