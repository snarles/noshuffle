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
        splitns[ii][jj] = splitns[ii][jj].split('.')
splitns = splitns[:len(listns)]

vowels = "AEIOU"
consonants = "BCDFGHJKLMNPQRSTVWXYZ0123456789"

