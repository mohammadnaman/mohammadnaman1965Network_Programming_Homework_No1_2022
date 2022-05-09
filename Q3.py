Rfile= 'C:\\Users\\محمد\\Documents\\qqqq.txt'
Wfile='C:\\Users\\محمد\\Documents\\ans.txt'
Qnfil=open(Rfile,'r')
Anfil=open(Wfile,'w')
l=[]
start=input("enter your name to start:")
Anfil.write(start+'\n')

for i in range(1,21):
    s=Qnfil.readline()
    q=print ("answer for the question number",i,":\n",s)
    ans=input('enter your answer:')
    l.append(ans)
    Anfil.write(ans+'\n')
    

print("your all answer:",l)
l.reverse()  
Rfile.close()
Wfile.close()
    
    