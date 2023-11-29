import numpy as np
import math
import matplotlib.pyplot as plt

import Reference_Data as RD
import Atmosphere as Atm

def n_cycle(t,r,n_t,n_c):
    g = RD.gamma
    r1 = r**((g-1)/g)
    n_cycle = ((t*(1-(1/r1))*n_t) - ((r1-1)/n_c))/(t-1-((r1-1)/n_c)) 
    return(n_cycle)


def n_0(n_prop,n_cycle):
    n_tr = RD.n_tr
    n_0 = n_prop * n_cycle * n_tr
    return(n_0)

def n_prop(h,M):
    FPR = RD.FPR
    g = RD.gamma
    g_1 = RD.gamma-1
    V = M*Atm.ISA(h)[4]
    P = Atm.ISA(h)[2]
    P0 = P + 0.5*Atm.ISA(h)[3]*(V**2)
    T = Atm.ISA(h)[1]

    M_j = math.sqrt((2/g_1)*((FPR*P0/P)**(g_1/g) -1))
    T_j = T * ((1+(0.5*g_1*M**2))/1+(0.5*g_1*M_j**2))*(FPR**(g_1/(g*RD.n_f)))

    n_prop = 2*((1+((M_j/M)*math.sqrt(T_j/T)))**-1)
    #print('nprop', g,g_1,V,P,P0,T)
    #print('nprop', n_prop, M,T,M_j, T_j)
    return(n_prop)