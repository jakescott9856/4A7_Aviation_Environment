import numpy as np
import math
import matplotlib.pyplot as plt

import Reference_Data as RD
import Atmosphere as Atm
import Lift_Drag as LD
import Engine as Eng
import Breguet as Brg

W_f = RD.W_fmp
W_p = RD.W_mp
W_e = RD.W_e

W_start = W_f + W_p + W_e
s_stage = 2000 #km
h= RD.h_cruise
nu = 1

W=W_start

n_cycle = Eng.n_cycle(RD.theta,RD.r,RD.n_t,RD.n_c)
"""Cruise"""
"""Loop"""

M = LD.Vels(W,h,nu)[0]
LD_ratio = LD.LD_ratio(nu)
n_prop = Eng.n_prop(h,M)
n_0 = Eng.n_0(n_prop,n_cycle)
W_fb = Brg.Breguet(n_0,LD_ratio,W,s_stage)[0]
H = Brg.Breguet(n_0,LD_ratio,W,s_stage)[2]
print(W_fb,H,LD_ratio,n_prop,n_cycle,n_0)