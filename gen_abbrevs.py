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
    if wt[0]==wt[1]:
        if ns[wt[0]] > 1:
            if (wt[0]==wt[2]):
                if (ns[wt[0]] > 2):
                    return [0,1,2]
                else:
                    return [0,0,1]
            else:
                return [0,1,0]
        else:
            return [0,0,0]
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
             ndistinct = 3 - int(st[0]==st[1]) - int(st[1]==st[2])
             ans=inc_wt(st,ns[wt[0]],ndistinct)
             if ans[0]==-1:
                 if ndistinct==1:
                     return [-1,-1,-1]
                 else:
                     return init_wt(ns[wt[0]],ndistinct-1)
             else:
                 return ans
        else:
             # first word has two
             return inc_st2(wt,st,ns)
    else:
        if (wt[1]==wt[2]):
             # second word has two
             # use the previous case, first word has two
             ans = inc_st2([0,0,1], [st[1],st[2],st[0]], [ns[wt[2]],ns[wt[0]]])
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
            if ns[wt[1]]> 1:
                return [0,1,st[2]+1]
            else:
                return [0,0,st[2]+1]
        else:
            return [-1,-1,-1]
    elif st[1] < (ns[wt[1]]-1):
        return [0,st[1]+1,st[2]]
    elif (st[2] < (ns[wt[2]]-1)):
        if ns[wt[1]]> 1:
            return [0,1,st[2]+1]
        else:
            return [0,0,st[2]+1]
    else:
        return [-1,-1,-1]
        

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
        if wt[0] < (nw-1):
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

def cumsum(ll):
    sum0 = 0
    cll = [0]*len(ll)
    for ii in range(len(ll)):
        sum0 = sum0+ll[ii]
        cll[ii]=sum0
    return cll

# syllable tracker to augmented syllable tracker
def st2ast(wt,st,ns):
    cns = [0]+cumsum(ns)
    ast = [0]*3
    for ii in range(3):
        ast[ii] = st[ii]+cns[wt[ii]]
    return ast

def ast2st(wt,ast,ns):
    cns = [0]+cumsum(ns)
    st = [0]*3
    for ii in range(3):
        st[ii] = ast[ii]-cns[wt[ii]]
    return st


# yield nw (number of words), ns (number of syllables) and nc (number of characters)
def ss2cts(ss):
    nw = len(ss)
    ns = [len(v) for v in ss]
    ss0 = ss[0]
    if len(ss) > 0:
        for ii in range(1,len(ss)):
            ss0=ss0+ss[ii]
    nc = [len(v) for v in ss0]
    return nw,ns,nc

def wsc2abbrev(ss,wt,st,ct):
    abbrev = ""
    for ii in range(3):
        abbrev=abbrev+ss[wt[ii]][st[ii]][ct[ii]]
    return abbrev

# returns a dict which contains all wt,st,ct combinations tried so far and most recent tried wt, and also the three letter abbrev
def init_adict(ss):
    adict = {}
    adict["ss"]=ss
    nw,ns,nc = ss2cts(ss)
    cur_nw = min(nw,3)
    wt = init_wt(nw,cur_nw)
    adict["wt"]=json.dumps(wt)
    adict["cur_nw"]=cur_nw
    temp={}
    temp["st"]=json.dumps([-1,-1,-1])
    adict[json.dumps(wt)] = temp
    inc_adict_st(adict)
    inc_adict_ct(adict)    
    return adict

# increments wt
def inc_adict_wt(adict):
    ss = adict["ss"]
    nw,ns,nc = ss2cts(ss)
    cur_nw = adict["cur_nw"]
    wt = json.loads(adict["wt"])
    wt = inc_wt(wt,nw,cur_nw)
    if wt[0]==-1:
        # decrement cur_nw and get the new wt
        cur_nw = cur_nw -1
        if cur_nw==0:
            cur_nw = min(nw,3)
        wt = init_wt(nw,cur_nw)
    adict["cur_nw"]=cur_nw
    adict["wt"] = json.dumps(wt)
    if adict.get(json.dumps(wt),"")=="":
        temp={}
        temp["st"]=json.dumps([-1,-1,-1])
        adict[json.dumps(wt)] = temp

# increments st
def inc_adict_st(adict):
    ss = adict["ss"]
    nw,ns,nc = ss2cts(ss)
    cur_nw = adict["cur_nw"]
    wt = json.loads(adict["wt"])
    temp = adict[adict["wt"]]
    # check we should reset
    if temp["st"]==json.dumps([-1,-1,-1]):
        st = init_st(wt,ns)
    else:
        # increment st
        st = inc_st(wt,json.loads(temp["st"]),ns)
    if temp.get(json.dumps(st),0)==0:
        temp[json.dumps(st)]=[]
    # check if st is valid: otherwise, go back to wt stage
    temp["st"]=json.dumps(st)
    if st[0]==-1:
        inc_adict_wt(adict)
        inc_adict_st(adict)

# increments ct
def inc_adict_ct(adict):
    ss = adict["ss"]
    nw,ns,nc = ss2cts(ss)
    cur_nw = adict["cur_nw"]
    wt = json.loads(adict["wt"])
    temp = adict[adict["wt"]]
    st = json.loads(temp["st"])
    ast = st2ast(wt,st,ns)
    # ct is never reset
    if len(temp[temp["st"]])==0:
        ct = init_st(ast,nc)
    else:
        oldct = json.loads(temp[temp["st"]][-1])
        ct = inc_st(ast,oldct,nc)
    temp[temp["st"]]=temp[temp["st"]] + [json.dumps(ct)]
    # check if ct is valid
    if ct[0]==-1:
        inc_adict_st(adict)
        inc_adict_ct(adict)

def inc_adict(adict):
    inc_adict_wt(adict)
    inc_adict_st(adict)
    inc_adict_ct(adict)

def cur_abbrev(adict):
    ss = adict["ss"]
    nw,ns,nc = ss2cts(ss)
    wt = json.loads(adict["wt"])
    temp = adict[adict["wt"]]
    st = json.loads(temp["st"])
    ct = json.loads(temp[temp["st"]][-1])
    return wsc2abbrev(ss,wt,st,ct)


# get the names

f = open('p_cardlist.txt','r')
listns = f.read().split('\n')
f.close()

ncards = len(listns)

f = open('annotated_cardlist.txt','r')
anncls = f.read().split('\n')
f.close()
splitns = [0]*ncards
splitns2=[0]*ncards
splitns3=[0]*ncards
for ii in range(ncards):
    splitns[ii] = anncls[ii].upper().replace('-',' ').split(' ')
    splitns2[ii] = anncls[ii].upper().replace(' OF ',' ').replace(' THE ',' ').replace('-',' ').split(' ')
    splitns3[ii] = anncls[ii].upper().replace(' OF ',' ').replace('-',' ').split(' ')
    for jj in range(len(splitns[ii])):
        splitns[ii][jj] = splitns[ii][jj].replace('AQ.','Q.').replace('CY.','Y.').split('.')
    for jj in range(len(splitns2[ii])):
        splitns2[ii][jj] = splitns2[ii][jj].replace('AQ.','Q.').replace('CY.','Y.').split('.')
    for jj in range(len(splitns3[ii])):
        splitns3[ii][jj] = splitns3[ii][jj].replace('AQ.','Q.').replace('CY.','Y.').split('.')
nws = [len(v) for v in splitns]
nws2 = [len(v) for v in splitns2]
nws3 = [len(v) for v in splitns3]

# demo
ss=splitns[5]
adict = init_adict(ss); cur_abbrev(adict)
inc_adict(adict); cur_abbrev(adict)




# abbrev all cards
nlvls = 5
fcodes = [""]*ncards
codes = [0]*nlvls
abvs = [0]*nlvls
adicts = [0]*ncards
past_abvs = []
remaining = []

# begin with 3+ letter cards
for ii in range(ncards):
    if (nws[ii] > 3) & (nws3[ii] > 2):
        if nws2[ii] > 2:
            ss = splitns2[ii]
        else:
            ss = splitns3[ii]
        adict = init_adict(ss)
        abv = cur_abbrev(adict)
        while abv in past_abvs:
            print "collision"
            inc_adict(adict)
            abv = cur_abbrev(adict)
        past_abvs = past_abvs + [abv]
        fcodes[ii] = abv
    else:
        remaining = remaining+[ii]
[(listns[ii],fcodes[ii]) for ii in range(ncards) if fcodes[ii]!='']

def update_codes(splitns,jj,codes,abvs,adicts,past_abvs,remaining):
    codes[jj]={}
    abvs[jj] = [0]*ncards
    for ii in remaining:
        ss = splitns[ii]
        if jj==0:
            adicts[ii] = init_adict(ss)
        abv = cur_abbrev(adicts[ii])
        while abv in past_abvs:
            inc_adict(adicts[ii])
            abv = cur_abbrev(adicts[ii])
        if codes[jj].get(abv,"")=="":
            codes[jj][abv]=[]
        codes[jj][abv] = codes[jj][abv] + [ii]
        abvs[jj][ii]=abv
    past_abvs = past_abvs + codes[jj].keys()
    # compute remaining
    new_remaining = []
    for ii in remaining:
        abv = abvs[jj][ii]
        if ii == codes[jj][abv][0]:
            fcodes[ii]=abv
        elif len(codes[jj][abv]) > 1:
            new_remaining = new_remaining+[ii]
        else:
            fcodes[ii]=abv
    jj=jj+1
    remaining = new_remaining
    return jj, codes, abvs, adicts, past_abvs, remaining

jj=0
jj, codes, abvs, adicts, past_abvs, remaining = update_codes(splitns,jj,codes,abvs,adicts,past_abvs,remaining)

fcodes_ann = [fcodes[ii]+" "+listns[ii] for ii in range(ncards)]
o = open('codelist.txt','w')
o.write('\n'.join(fcodes_ann))
o.close()
fcodesann2 = sorted(fcodes_ann)
o = open('codelist2.txt','w')
o.write('\n'.join(fcodesann2))
o.close()
    
