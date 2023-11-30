import numpy as np
import math
import matplotlib.pyplot as plt

import Reference_Data as RD


def Breguet(n_0,LD_ratio,Ms_start,s_stage):
    H = RD.LCV * n_0 * LD_ratio /RD.g 
    Ms_fb = Ms_start*(1-math.exp(-s_stage/H))
    Ms_end = Ms_start - Ms_fb
    #print(H,RD.LCV, n_0, LD_ratio, RD.g)
    return(Ms_fb,Ms_end,H)