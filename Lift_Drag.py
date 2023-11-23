import numpy as np
import math
import matplotlib.pyplot as plt

import Reference_Data as RD
import Atmosphere as Atm

def LD_ratio(nu):
    beta_star = 2*math.sqrt(RD.K_1*RD.K_2)
    beta = 0.5*beta_star*((nu**2) + (1/nu**2))
    LD_ratio = 1/beta
    return(LD_ratio)

def Vels(W,h,nu):
    V_e_star = (W/(0.5*Atm.Ro_sl*RD.A_wing))**0.5 *(RD.K_2/RD.K_1)**0.25

    V_e = nu * V_e_star

    sigma = Atm.ISA(h)[3]/Atm.Ro_sl
    V = V_e / (sigma**0.5)

    M = V/Atm.ISA(h)[4]

    return(M,V,V_e_star,V_e)


#print(Vels(RD.W_mto,RD.h_cruise,1))