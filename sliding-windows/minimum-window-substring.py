s="OUZODYXAZV"
t="XYZ"

n=len(t)
result=""
for i in range(len(s)):
    if s[i] in t:
        count=0
        for j in range(i,len(s)):
            count+=1
            if count<=n:
                result+=s[j]
print(result)
            

