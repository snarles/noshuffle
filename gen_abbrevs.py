import json

# initialize word tracker
def init_wt(nw,cur_nw):
    if cur_nw==1:
        if nw > 0:
            return [0,0,0]
        else:
            return [-1,-1,-1]
    if cur_nw==2:
        if nw > 1:
            return [0,0,1]
        else:
            return [-1,-1,-1]
    if cur_nw==3:
        if nw > 2:
            return [0,1,2]
        else:
            return [-1,-1,-1]

# initialize syllable tracker
def init_st(wt,ns):
    if (wt[0]==wt[1]):
        if (ns[wt[0]] > 1):
            if (wt[0]==wt[2]):
                if (ns[wt[0]] > 2):
                    return [0,1,2]
                else:
                    return [-1,-1,-1]
            else:
                return [0,1,0]
        else:
            return [-1,-1,-1]
    else:
        if (wt[1]==wt[2]):
            if (ns[wt[1]] > 1):
                return [0,0,1]
            else:
                return [-1,-1,-1]
        else:
            return [0,0,0]

# increment syllable tracker
def inc_st(wt,st,ns):
    if (wt[0]==wt[1]):
        if (wt[0]==wt[2]):
             # three in one word
             # use the word tracker to do this
        else:
             # first word has two
    else:
        if (wt[1]==wt[2]):
             # second word has two
        else:
             # three different words

# increment word tracker
def inc_wt(wt,nw,cur_nw):
    if cur_nw ==1:
        if wt[0] < nw:
            return [wt[0]+1,wt[0]+1,wt[0]+1]
        else:
            return [-1,-1,-1]
    if cur_nw ==2:
        if wt[0]==wt[1]:
            return [wt[0],wt[2],wt[2]]
        elif wt[0] < (wt[2]-1):
            return [wt[0]+1,wt[0]+1,wt[2]]
        elif wt[2] < (nw-1):
            return [0, wt[2]+1,wt[2]+1]
        else:
            return [-1,-1,-1]
    if cur_nw ==3:
        if wt[0] < (wt[1]-1):
            return [wt[0]+1,wt[1],wt[2]]
        elif wt[1] < (wt[2]-1):
            return [0,wt[1]+1,wt[2]]
        elif wt[2] < (nw-1):
            return [0,1,wt[2]+1]
        else:
            return [-1,-1,-1]

def test_inc_wt(nw,cur_nw):
    wt = init_wt(nw,cur_nw)
    print wt
    while json.dumps(wt) != json.dumps([-1,-1,-1]):
        wt = inc_wt(wt,nw,cur_nw)
        print wt

def abbrevs(ss):


# get the names

f = open('p_cardlist.txt','r')
listns = f.read().split('\n')
f.close()

f = open('annotated_cardlist.txt','r')
splitns = f.read().split('\n')
f.close()
for ii in range(len(splitns)):
    splitns[ii] = splitns[ii].upper().replace('-',' ').split(' ')
    for jj in range(len(splitns[ii])):
        splitns[ii][jj] = splitns[ii][jj].replace('AQ.','Q.').replace('CY.','Y.').split('.')
splitns = splitns[:len(listns)]

vowels = "AEIOU"
consonants = "BCDFGHJKLMNPQRSTVWXYZ0123456789"

ss=splitns[2]
nw = len(ss)
ns = [len(v) for v in ss]
cur_nw = min(3,nw)
cur_char=1

wt = init_wt(nw,cur_nw)
st = init_st(wt,ns)
wtst_map = {}
wtst_map[json.dumps(wt)] = [json.dumps(st)]


    
