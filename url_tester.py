import requests
import sys

f = open('C://Users/yogen/Desktop/lyft.txt')
x =  []
new_x= []
for i in f:
   x.append(i.split('\n')[0])
f.close()



for j in x:
    s = "http://" + j    
    try:        
        r = requests.get(s)
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        continue
    else:
        st = r.status_code
        if(st == 200):
            new_x.append(s+" "+ str(st))

new_file = open('C://Users/yogen/Desktop/lyft.txt2','w')
for k in new_x:
    new_file.write(k+"\n")

new_file.close()

