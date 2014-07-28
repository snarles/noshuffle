
f = open('cardlist.txt','r')
ff = f.read().split('\n')
f.close()

import string

# get raw names
rawns = {}
splitns = {}
listns = {}
count = 0
for ii in range(len(ff)-1):
    ss = ff[ii]
    if (ss[0]=='*'):
        sss = ss.split(' ')[2:]
        ss2 = ''.join(sss)
        ss3 = filter(str.isalnum, ss2).upper()
        if rawns.get(ss3,0)==0:
            count = count+1            
            listns[count] = ss3 
            rawns[ss3] = 1
            ss4 = '91919'.join(sss).upper()
            ss5 = filter(str.isalnum, ss4)
            ss6 = ss5.split('91919')
            splitns[count] = ss6


clocks = range(count)
winds = range(count)
for ii in range(count):
    ss = listns[ii+1]
    sum = 0
    for cc in ss:
        sum = sum+ord(cc)-64
    clocks[ii] = sum % 12
    sum = 0
    for j in range(len(ss)):
        if j % 2==1:
            sum = sum+ord(ss[j])-64
    winds[ii] = sum % 12

