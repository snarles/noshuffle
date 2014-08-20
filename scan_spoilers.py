
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
races = sorted(list(set(races))) 
pf = "']=''\nracemap['".join(races)
o = open('temp.txt','w')
o.write(pf)
o.close()


# Angel Command, Aquan, Armored Dragon, Attack Raptor, Battle Sphere, Beast Kin, Berserker, Blaze Champion, Brain Jacker, Burn Belly, Celestial Dragon, Chimera, Colossus, Corrupted, Cyber Complex, Cyber Lord, Cyber Virus, Dark Lord, Drakon, Dread Mask, Dune Gecko, Earth Eater, Earthstrike Dragon, Enforcer, Evil Toy, Fire Bird, Flying Fungus, Fractal, Human, Inferno Complex, Invader, Leviathan, Living City, Mecha Thunder, Megabug, Melt Warrior, Mimic, Monarch, Mystic, Primal Champion, Riptide Champion, Rock Brute, Rot Worm, Shadow Champion, Sky Weaver, Skyforce Champion, Snow Sprite, Specter, Spirit Quartz, Spirit Totem, Star Sentinel, Stomper, Storm Patrol, Survivor, Tarborg, Terror Dragon, Tree Kin, Trench Hunter, Tsunami Dragon, Tusker, Undertow Engine, Void Spawn, Wild Veggie, Zombie
# manually set races
racemap={}
racemap['Angel Command']='AnglCmd'
racemap['Aquan']='Aqn'
racemap['Armored Dragon']='ArmDrgn'
racemap['Attack Raptor']='AtkRptr'
racemap['Battle Sphere']='BtlSphr'
racemap['Beast Kin']='BstKn'
racemap['Berserker']='Bskr'
racemap['Blaze Champion']='BlzChmpn'
racemap['Brain Jacker']='BrnJkr'
racemap['Burn Belly']='BrnBly'
racemap['Celestial Dragon']='CelsDrgn'
racemap['Chimera']='Chmra'
racemap['Colossus']='Colss'
racemap['Corrupted']='Corptd'
racemap['Cyber Complex']='CybCplx'
racemap['Cyber Lord']='CybLrd'
racemap['Cyber Virus']='CybVrs'
racemap['Dark Lord']='DkLd'
racemap['Drakon']='Drakn'
racemap['Dread Mask']='DrdMsk'
racemap['Dune Gecko']='DunGko'
racemap['Earth Eater']='ErthEatr'
racemap['Earthstrike Dragon']='EstDrgn'
racemap['Enforcer']='Enfcr'
racemap['Evil Toy']='EvlToy'
racemap['Fire Bird']='FirBrd'
racemap['Flying Fungus']='FlyFgs'
racemap['Fractal']='Frac'
racemap['Human']='Hum'
racemap['Inferno Complex']='InfCplx'
racemap['Invader']='Ivdr'
racemap['Leviathan']='Lvth'
racemap['Living City']='LvgCit'
racemap['Mecha Thunder']='MecThndr'
racemap['Megabug']='Mgbug'
racemap['Melt Warrior']='MltWrr'
racemap['Mimic']='Mmc'
racemap['Monarch']='Monrch'
racemap['Mystic']='Mystic'
racemap['Primal Champion']='PrmChmpn'
racemap['Riptide Champion']='RptChmpn'
racemap['Rock Brute']='RokBrt'
racemap['Rot Worm']='RotWrm'
racemap['Shadow Champion']='ShdChmpn'
racemap['Sky Weaver']='SkyWea'
racemap['Skyforce Champion']='SkfcChmpn'
racemap['Snow Sprite']='SnSprite'
racemap['Specter']='Spctr'
racemap['Spirit Quartz']='SptQtz'
racemap['Spirit Totem']='SptTtm'
racemap['Star Sentinel']='StrSntnl'
racemap['Stomper']='Stmpr'
racemap['Storm Patrol']='StrmPtrl'
racemap['Survivor']='Survvr'
racemap['Tarborg']='Tarbg'
racemap['Terror Dragon']='TrrDrgn'
racemap['Tree Kin']='TreeKn'
racemap['Trench Hunter']='TrcHnt'
racemap['Tsunami Dragon']='TsuDrgn'
racemap['Tusker']='Tskr'
racemap['Undertow Engine']='UndtEngn'
racemap['Void Spawn']='VdSpwn'
racemap['Wild Veggie']='WldVgg'
racemap['Zombie']='Zom'

racemap2 = {}
for ky in racemap.keys():
    racemap2[ky.upper()] = racemap[ky]
racemap2['CREATURES'] = 'allies'

# fill in race and level
for ii in range(ncards):
    dentry = database[ii]
    spoiler = database[ii]["spoiler"]
    l1 = spoiler[0]
    lv = int(l1.split(' - Level ')[1])
    dentry["Level"] = lv
    l2 = spoiler[1]
    if l2=="Spell":
        dentry["Type"]="Spell"
        dentry["Power"]=0
        rest = spoiler[:]
    else:
        dentry["Type"]="Creature"
        temp1 = l2.split(" - ")
        temp2 = temp1[1].split("/")
        temp3 = [racemap[tt] for tt in temp2]
        dentry["Races"]=temp3
        #power
        dentry["Power"] = int(temp1[2].split(' ')[0])
    dentry["Special"]=[]


def process_special(spoiler):
    special = []
    # process special text
    if len(spoiler) > 2:
        for sp in spoiler[2:]:
            sp = process_special1(sp)
            special=special+[sp]
    return special

def process_special1(sp):
    # kill the opening label
    if ' - ' in sp:
        sp = sp.split(' - ')[1]
    if '\xe2\x80\x94' in sp:
        sp = sp.split(' \xe2\x80\x94 ')[1]
    # kill reminder text
    if '(' in sp:
        sp1 = sp.split('(')
        sp=''
        for ss in sp1:
            if not ')' in ss:
                sp=sp+ss
            else:
                sp=sp+ss.split(')')[1]
    if sp[:14]=='Double Breaker':
        sp='DBkr'
    elif sp[:7]=='Blocker':
        sp='Blkr'
    elif sp[:10]=='Skirmisher':
        sp='Skmshr'
    elif sp[:5]=='Guard':
        sp='Grd'
    elif sp[:12]=='Shield Blast':
        sp='SB'
    elif sp=="This creature can't be blocked.":
        sp='Unblockable'
    elif sp=="This creature can't be blocked by creatures that have less power than it.":
        sp='UnChumpBlockable'
    elif sp[:6]=='Slayer':
        sp = 'Slay'
    elif sp.upper()=='THIS CREATURE ATTACKS EACH TURN IF ABLE.':
        sp = 'MustAtk'
    elif sp[:11]=='Fast Attack':
        sp = 'Haste'
    elif sp.upper()=='THIS CREATURE CAN ATTACK UNTAPPED CREATURES.':
        sp = 'AtkUntapped'
    elif sp[:17].upper()=='POWERFUL ATTACK +':
        no = sp.split('+')[1]
        sp = 'Atk+'+no
    elif sp.upper()=='IF THIS CREATURE WOULD BE BANISHED, RETURN IT TO YOUR HAND INSTEAD.':
        sp = 'DIES: self-bounce'
    else:
        sp=process_special2(sp)
    return sp

def process_special2(sp):
    ftype=''
    # check ETB, DIES, ATK, WIN, LOSE conditions
    if sp[:30]=='Whenever this creature attacks':
        ftype='ATKS'
        sp = sp[32:]
    elif sp[:29].upper()=='WHENEVER THIS CREATURE BLOCKS':
        ftype='BLOCKS'
        sp=sp[31:]
    elif sp[:26]=='When this creature attacks':
        ftype='ATKS'
        sp = sp[28:]
    elif sp[:41]=='When this creature enters the battle zone':
        ftype='ETB'
        sp = sp[43:]
    elif sp[:32].upper()=='WHEN THIS CREATURE WINS A BATTLE':
        ftype ='WINS'
        sp = sp[34:]
    else:
        # special effects which occur commonly
        if sp=='This creature can attack tapped creatures on the turn it enters the battle zone.':
            return 'ETB: attack tapped'
    sp = process_special3(sp)
    # attach trigger conditions
    if ftype != '':
        sp = ftype+": "+sp
    return sp

def process_special3(sp):
    # effects
    pre = ''
    sp = sp.upper()
    if sp[:7]=='YOU MAY':
        pre = 'may '
        sp=sp[8:]
    if sp[:11]=='DRAW A CARD':
        sp = 'draw 1'
    elif sp[:12]=='DRAW 2 CARDS':
        sp = 'draw 2'
    elif sp[:9]=='BANISH IT':
        sp = 'dies'
    elif sp[:22]=='Return target creature'.upper():
        if 'LEVEL' in sp.upper():
            sp = 'bounce lv' + sp.upper().split(' LEVEL ')[1][0]
        else:
            sp = 'bounce'
    elif sp[:28]=='Banish target enemy creature'.upper():
        if 'LEVEL' in sp.upper():
            sp = 'killEnemy lv' + sp.upper().split(' LEVEL ')[1][0]
        elif 'POWER' in sp.upper():
            temp = sp.upper().split(' POWER ')[1]
            sp = 'killEnemy power' + temp.split(' ')[0]
        else:
            sp = 'killEnemy'
    elif (sp[:10]=='PUT TARGET') & (sp[-21:]=="OPPONENT'S MANA ZONE."):
        new_sp='manabind'
        if 'ENEMY' in sp:
            new_sp = new_sp+' enemy'
        if 'LEVEL' in sp.upper():
            new_sp = new_sp+' lv '+sp.upper().split(' LEVEL ')[1][0]
        sp = new_sp
    elif sp[:25]=='TAP TARGET ENEMY CREATURE':
        sp = 'tap enemy'
    elif sp=='banish target untapped enemy creature.'.upper():
        sp = 'deathSmoke'
    elif sp=='YOUR OPPONENT CHOOSES AND DISCARDS A CARD.':
        sp = 'oppDiscard 1'
    elif sp=='PUT THE TOP CARD OF YOUR DECK INTO YOUR MANA ZONE.':
        sp = 'ramp 1'
    elif sp[:18]=='EACH OF YOUR OTHER':
        temp = sp[19:].split(' GETS ')
        sp = 'lord '+racemap2[temp[0]]+temp[1]
    sp = pre+sp
    return sp


