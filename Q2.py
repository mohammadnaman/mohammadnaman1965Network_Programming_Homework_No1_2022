l=[]
intnum=int(input("enter integar number:"))

   #l1=[intnum]

n=intnum

for i in range(intnum) :
    d=n//2
    by=str(n%2)
    l.append(by)
               
             #l1.append(d)
               
    n=n//2
               
             #  if n==0:
              #     break

l.reverse()  
           #print(l1)     
           #print(l)

print("converts a decimal number into its equivalent binary number:","".join(l))