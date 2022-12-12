#Find the second largest number and its index in an array.

n=int(input("Enter N:"))
a=[]
for i in range(n):
    a.append(int(input("Enter a Number:")))
max=0
index=0
new_max=0
for i in range(n):
    if a[i]>=max:
        max=a[i]
print(max)

for i in range(n):
    if(a[i]==max):
        continue
    else:
        if a[i]>=new_max:
            new_max=a[i]
            index=i
print(f"index:{index} Second Max:{new_max}")