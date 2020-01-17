domain = input("Enter Domain name")
f_path = "C://Users/yogen/Desktop/"
x = []
s = []

f = open(f_path+domain+'/hosts.txt','r')
for i in f:
    x.append(i)

f.close()

for j in range(len(x)):
    s.append(x[j].split(',')[0])

new_f = open(f_path+domain+'/domain_sorted.txt','w')

for k in s:
    new_f.write(k+'\n')

new_f.close()

