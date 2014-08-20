
# read cards
f = open('p_cardlist.txt','r')
listns = f.read().split('\n')
f.close()
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

ii = 1
f = open(spoiler_fs[ii],'r')
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
formatted = formatted[1:]

nf = len(formatted)
# check that card names are correct
cns = [formatted[ii][0].split(' - ')[0] for ii in range(nf)]
[ss for ss in cns if not (stripAlph(ss) in rlistns)]



