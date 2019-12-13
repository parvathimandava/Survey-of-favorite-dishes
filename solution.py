input1=3
 
input2=[-1,9,0,5,-4,-6,-3]
a= []
max=input2[0]
l=len(input2)
for i in range(1,l):
    if(input2[i]>=0):
        a.append(input2[i])
    i=i+1
n=len(a)
for i in range(0,n):
    max=max+(i+2)*a[i];
    i=i+1
print(max)
