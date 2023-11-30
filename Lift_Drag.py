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
    K_ratio = (RD.K_2/RD.K_1)**0.25
    V_e_star = ((W/(0.5*Atm.Ro_sl*RD.A_wing))**0.5) * K_ratio

    V_e = nu * V_e_star

    sigma = Atm.ISA(h)[3]/Atm.Ro_sl
    V = V_e / (sigma**0.5)
    a = Atm.ISA(h)[4]
    M = V/a
    #print("vels",W, M,V_e_star,V_e,sigma,V,a)
    return(M,V,V_e_star,V_e)

def Cl(W,h,V): 
    Ro = Atm.ISA(h)[3]
    Cl = W/(0.5*Ro*(V**2)*RD.A_wing)
    return(Cl)

def Wingloading(W):
    WL_KN = W / RD.A_wing #KN/M2
    WL_KG = WL_KN / RD.g
    return (WL_KN, WL_KG)

"""
def nu(W,h,M):
    a = Atm.ISA(h)[4]
    V = M * a
    sigma = Atm.ISA(h)[3]/Atm.Ro_sl
    V_e = V * (sigma**0.5)
    V_e_star = ((W/(0.5*Atm.Ro_sl*RD.A_wing))**0.5) *((RD.K_2/RD.K_1)**0.25)
    nu = V_e / V_e_star
    return(nu,sigma)
"""