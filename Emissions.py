import numpy as np
import math
import matplotlib.pyplot as plt

import Reference_Data as RD
import Atmosphere as Atm

def EI_nox(M,h,Ms_fb,r,n_c):
    g = RD.gamma
    g_1 = g -1
    r1 = r**((g-1)/g)
    T_a = Atm.ISA(h)[1]
    T_02 = T_a * (1 + ((g_1/2)*M**2))
    T_03 = T_02 * (1 + ((r1-1)/n_c))
    EI_nox = 0.011445 * math.exp(0.00676593*T_03) #gNOx/kg air
    Ms_air = Ms_fb * RD.AF_ratio*2 #kg air
    Ms_nox = EI_nox * Ms_air
    return(Ms_nox, EI_nox)

def EI_co2(Ms_fb):
    EI_co2 = 3088 #gCO2/kg fuel
    Ms_co2 = EI_co2 * Ms_fb
    return(EI_co2, Ms_co2)

def FBPR(s,H,W_e,W_p): #Wf/sWp
    k =RD.k
    FBPR = (1/s) * (1 + (W_e/W_p)) * ((1-math.exp(-s/H) +k)/(math.exp(-s/H) -k))
    return FBPR