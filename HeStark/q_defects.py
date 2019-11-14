#! python
# -*- coding: utf-8 -*-

#Created on Wed 01 Nov 2019
#@author: Klaudia Gawlas, UNIVERSITY COLLEGE LONDON.

# Routine to calculate the quantum defects of the triplet Rydberg states of helium
# From Martin, Phys. Rev. A, vol. 36, pp. 3575-3589 (1987)

def He_triplet_defect(n,ell):
    a=[0.29665648771,0.06836028379,0.002891328825,0.00044737927,0.00012714167,0.000048729846,0.000023047609] #s,p,d,f,g,h,i
    b=[0.038296666,-0.018629228,-0.0063577040,-0.001739217,-0.000796484,-0.0004332281,-0.0002610672] #s,p,d,f,g,h,i
    c=[0.0075131,-0.01233275,0.00033670,0.00010478,-0.00000985,-0.00000810,-0.00000404] #s,p,d,f,g,h,i
    d=[-0.0045476,-0.0079527,+0.0008395,0.0000331,-0.000019,0,0] #s,p,d,f,g,h,i
    
    if ell <=6:
        m=n-a[ell]
        defect = a[ell] + b[ell]*(m**-2) + c[ell]*(m**-4) + d[ell]*(m**-6)
    else:
        defect=0
    return defect