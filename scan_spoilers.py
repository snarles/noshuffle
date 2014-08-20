
# read cards
f = open('p_cardlist.txt','r')
listns = f.read().split('\n')
f.close()
if listns[-1]=='':
    listns = listns[:-1]
ncards = len(listns)
f = open('codelist.txt','r')
temp = f.read().split('\n')
f.close()
codes = [ss[:4] for ss in temp]
def stripAlph(ss):
    return ss.replace('-','').replace(' ','').replace("'",'').replace(',','').upper()
rlistns = [stripAlph(ss) for ss in listns]


civs = ['W','U','B','R','G']
spoiler_fs = ['spoiler_w.txt','spoiler_u.txt','spoiler_b.txt','spoiler_r.txt','spoiler_g.txt']

database=['']*ncards

for iii in range(5):
    f = open(spoiler_fs[iii],'r')
    temp = f.read().split('\n')
    f.close()

    formatted = []
    ii = 0
    spoilet = []
    while ii < len(temp):
        if ' - Level ' in temp[ii]:
            formatted = formatted + [spoilet]
            spoilet = []
        spoilet = spoilet + [temp[ii]]
        ii=ii+1
    formatted = formatted + [spoilet]
    formatted = formatted[1:]

    nf = len(formatted)
    # check that card names are correct
    cns = [formatted[ii][0].split(' - ')[0] for ii in range(nf)]
    print [ss for ss in cns if not (stripAlph(ss) in rlistns)]

    cur_civ = civs[iii]
    for ii in range(nf):
        no = rlistns.index(stripAlph(cns[ii]))
        # create database if necessary
        if database[no]=='':
            database[no]={}
            database[no]["spoiler"] = formatted[ii]
            database[no]["civs"] = []
            database[no]["name"]=listns[no]
        dentry = database[no]
        # enter civ info in database
        dentry["civs"]=dentry["civs"]+[iii]

# check which are missing
[listns[ii] for ii in range(ncards) if database[ii]=='']

races=[]
# extract races
for ii in range(ncards):
    spoiler = database[ii]["spoiler"]
    l2 = spoiler[1]
    if l2=="Spell":
        0
    else:
        temp1 = l2.split(" - ")[1]
        temp2 = temp1.split("/")
        races = races + temp2
