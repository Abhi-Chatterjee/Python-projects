import slate3k as slate
f=open('E:/Programming/PDF Extract/file1.pdf','rb')
c=0
i=0
t=slate.PDF(f)
t[0]=t[0].replace('\n',' ')
ar=t[0].split(' ')
c=c+ar.count('Amreeta')
g=open('E:/Programming/PDF Extract/file2.pdf','rb')
i=0
t=slate.PDF(g)
t[0]=t[0].replace('\n',' ')
ar=t[0].split(' ')
c=c+ar.count('Amreeta')
print("No of occurences is ",c)
