x = int(input("Enter x value :"))
y = int(input("Enter y value :"))
z = int(input("Enter z values :2"))
n = int(input("Enter the value count that should not be taken : "))
l=[]
for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k)==n:
                    continue
                l.append([i,j,k])
print(l)
