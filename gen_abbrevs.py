import json

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

wt = init_wt(cur_nw)
st = init_st(wt,ns)
wtst_map = {}
wtst_map[json.dumps(wt)] = [json.dumps(st)]



# initialize word tracker
def init_wt(cur_nw):
    if cur_nw==1:
        return [0,0,0]
    if cur_nw==2:
        return [0,0,1]
    if cur_nw==3:
        return [0,1,2]

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

# increment syllable tracker given cached hash map of words and syllables



# increment word tracker
def inc_wt(wt,nw,cur_nw):
    if cur_nw ==2:
        if wt[0]==wt[1]:
            return [wt[0],wt[2],wt[2]]
        elif min(wt) < (max(wt)-1):
            m1 = min(wt)+1
            m2 = max(wt)
            return [m1,m1,m2]
        else:
            return [-1,-1,-1]

def abbrevs(ss):
    
