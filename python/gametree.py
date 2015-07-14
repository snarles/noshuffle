
def qrec(p,K,nits):
    q=0.0
    u=0.0
    for i in range(nits):
        q = (1-p)*(1-(1-u)**K)
        u = p+(1-p)*(q**K)
        print (q,u)
    pdraw = 1-q-u
    pf2 = p+(1-p)*(1-(1-p)**K)
    return pdraw,pf2,1-pdraw-pf2

def plys(p,K):
    pwin1 = 1-(1-p)**K
    pwin2 = pwin1**K
    pwin3 = 1-(1-pwin2)**K
    pwin4 = pwin3**K
    return 1/pwin1, 1/pwin2 + 1,1/pwin3 + 2,1/pwin4+3

import numpy as np
import numpy.random as nr


def selX(xx, view, nits):
    res = [0.]*nits
    for ii in range(nits):
        tval = nr.normal(0,1,xx/view)
        oval = nr.normal(0,1.0/view,xx/view)+tval
        idx = np.argmax(oval)
        res[ii]=tval[idx]
    return np.mean(res),np.std(res)



    
