import json

def all_perms(perm):
    return [[perm[0],perm[1],perm[2]],
        [perm[0],perm[2],perm[1]],
        [perm[1],perm[0],perm[2]],
        [perm[1],perm[2],perm[0]],
        [perm[2],perm[0],perm[1]],
        [perm[2],perm[1],perm[0]]]


def inc_perm(perm, bounds):
    if (perm[0] < perm[1]) & (perm[0] < (bounds[0]-1)):
        return [perm[0]+1,perm[1],perm[2]]
    elif (perm[1] < perm[2]) & (perm[1] < (bounds[1]-1)):
        return [0,perm[1]+1,perm[2]]
    elif (perm[2] < (bounds[2]-1)):
        return [0,0,perm[2]+1]
    else:
        return [-1,-1,-1]

def test_inc_perm(perm,bounds):
    print perm
    while perm[0] != -1:
        perm = inc_perm(perm,bounds)
        print perm


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
             return inc_wt(st,ns[wt[0]],3)
        else:
             # first word has two
             return inc_st2(wt,st,ns)
    else:
        if (wt[1]==wt[2]):
             # second word has two
             # use the previous case, first word has two
             ans = inc_st([0,0,1], [st[1],st[2],st[0]], [ns[wt[2]],ns[wt[1]]])
             return [ans[2],ans[0],ans[1]]
        else:
             # three different words
             return inc_st3(wt,st,ns)

def inc_st2(wt,st,ns):
    # first word has two
    if st[0] < (st[1]-1):
        return [st[0]+1,st[1],st[2]]
    elif (st[2] < (st[1]-1)) & (st[2] < (ns[wt[2]]-1)):
        return [0,1,st[2]+1]
    elif st[1]==ns[wt[1]]:
        if st[2] < (ns[wt[2]]-1):
            return [0,1,st[2]+1]
        else:
            return [-1,-1,-1]
    else:
        return [0,st[1]+1,st[2]]

def test_inc_st2(wt,st,ns):
    print st
    while st[0]!=-1:
        st = inc_st2(wt,st,ns)
        print st


def inc_st3_sub(wt,st,perm,ns):
    ap = all_perms(perm)
    for cand in ap:
        flag1=(cand[0] > st[0]) | ((cand[0]==st[0]) & (cand[1] > st[1]))
        flag1=flag1 | ((cand[0]==st[0]) & (cand[1]==st[1]) & (cand[2] > st[2]))
        flag2=(cand[0] < ns[wt[0]]) & (cand[1] < ns[wt[1]]) & (cand[2] < ns[wt[2]])
        if (flag1 & flag2):
            return cand
    return [-1,-1,-1]

def inc_st3(wt,st,ns):
    perm = sorted(st)
    bounds = sorted([ns[wt[0]],ns[wt[1]],ns[wt[2]]])
    ans = inc_st3_sub(wt,st,perm,ns)
    if ans[0]==-1:
        return inc_st3_sub(wt,[0,0,0],inc_perm(perm,bounds),ns)
    else:
        return ans

def test_inc_st3(wt,st,ns):
    print st
    while st[0] != -1:
        st = inc_st3(wt,st,ns)
        print st

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

def test_inc_st(wt,ns):
    st = init_st(wt,ns)
    print st
    while json.dumps(st) != json.dumps([-1,-1,-1]):
        st = inc_st(wt,st,ns)
        print st


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


    
