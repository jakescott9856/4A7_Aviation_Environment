import numpy as np
import math
import matplotlib.pyplot as plt

import Reference_Data as RD
import Atmosphere as Atm
import Lift_Drag as LD
import Engine as Eng
import Breguet as Brg
import Emissions as Em
Ms_f_start = RD.Ms_fmp *1000 #KG
Ms_p = RD.Ms_mp *1000 #KG
Ms_e = RD.Ms_e *1000 #KG

Ms_start = Ms_f_start + Ms_p + Ms_e
W_start = Ms_start * RD.g

s_total = 8000 #km
h= RD.h_cruise
nu = 1

W = W_start
Ms = Ms_start
Ms_f = Ms_f_start

n_cycle = Eng.n_cycle(RD.theta,RD.r,RD.n_t,RD.n_c)

s_section = 10 #km
s_cumulative = 0

E_co2 = 0.0
E_nox = 0.0
#Takeoff ---------------------------
Ms_fb = Ms_start * RD.k
Ms_f = Ms_f - Ms_fb
W = W - (Ms_fb*RD.g)
M = LD.Vels(W,h,nu)[0]
print(round(s_cumulative),round(Ms_fb,2), round(Ms_f,2) )

#Cruise Loop -----------------------
print("Start of Cruise ------")
while Ms_f > 0:
    WL_KG = LD.Wingloading(W)[1]
    h = LD.Heights(W,M,nu)
    V = LD.Vels(W,h,nu)[1]

    LD_ratio = LD.LD_ratio(nu)

    n_prop = Eng.n_prop(h,M)
    n_0 = Eng.n_0(n_prop,n_cycle)

    H = Brg.Breguet(n_0,LD_ratio,W,s_section)[2]
    Ms_fb = Brg.Breguet(n_0,LD_ratio,Ms,s_section)[0]
    Ms_f = Ms_f - Ms_fb
    W = W - (Ms_fb*RD.g)
    s_cumulative = s_cumulative + s_section
    
    print(round(s_cumulative), round(Ms_f,2),round(Ms_fb/s_section,2),round(M,2), round(LD_ratio,2), round(n_0,2),round(n_prop,2), round(h,2) )

print(E_nox,E_co2)
#Landing -----------------------

#Emissions ----------------------
E_nox = E_nox + Em.EI_nox(M,h,Ms_fb)[0]
E_co2 = E_co2 + Em.EI_co2(Ms_fb)[0]

"""
print("Altitude:", h, "KM, WingLoading:", round(WL_KG,3),"KG/M2")
print("Mach no:", round(M,3))
print("n_prop:", round(n_prop,3), "n_cycle:", round(n_cycle,3), "n_0:", round(n_0,3))
print("LD Ratio:", round(LD_ratio,3),"Cl", round(Cl,3))
print("Range Par", round(H,3),"KM, Fuel Burn:", Ms_fb,"Kg")"""