
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
        sss = ss.replace('-',' ').split(' ')[2:]
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

# three letter abbreviations

abbrevs = {}
for ii in range(count):
    ll = splitns[ii+1]
    nm = listns[ii+1]
    # check for exactly three words
    if (len(ll) == 3):
        pos = [0,0,0]
        lens = [len(ll[0]), len(ll[1]), len(ll[2])]
        maxrng=[0,0,0]
        flag = True
        while flag:
            cand = ll[0][pos[0]]+ll[1][pos[1]]+ll[2][pos[2]]
            if abbrevs.get(cand,0)==0:
                flag=False
            else:
                if pos==maxrng:
                    mmr = max(maxrng)
                    if maxrng[1] < mmr & maxrng[1] < lens[1]:
                        maxrng[1]=maxrng[1]+1
                        pos[1]=pos[1]+1
                        pos[2]=0
                        pos[0]=0
                    elif maxrng[0] < mmr & maxrng[0] < lens[0]:
                        maxrng[0]=maxrng[0]+1
                        pos[0]=pos[0]+1
                        pos[1]=0
                        pos[2]=0
                    elif maxrng[2] < lens[2]:
                        maxrng[2]=maxrng[2]+1
                        pos[2]=pos[2]+1
                        pos[0]=0
                        pos[1]=0
                    elif maxrng[1] < lens[1]:
                        maxrng[1]=maxrng[1]+1
                        pos[1]=pos[1]+1
                        pos[0]=0
                        pos[2]=0
                    elif maxrng[0] < lens[0]:
                        maxrng[0]=maxrng[0]+1
                        pos[0]=pos[0]+1
                        pos[1]=0
                        pos[2]=0                                       
                elif pos[2] < maxrng[2]:
                    pos[2]=pos[2]+1
                elif pos[1] < maxrng[1]:
                    pos[1]=pos[1]+1
                    pos[2]=0
                elif pos[0] < maxrng[0]:
                    pos[0]=pos[0]+1
                    pos[1]=0
                    pos[2]=0
        abbrevs[cand]=ii+1


        
