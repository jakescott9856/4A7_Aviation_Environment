import numpy as np
import math
import matplotlib.pyplot as plt

import Reference_Data as RD


def Breguet(n_0,LD_ratio,W_start,s_stage):
    H = RD.LCV * n_0 * LD_ratio /RD.g 
    W_end = W_start/math.exp(s_stage/H)
    W_fb = W_start - W_end
    return(W_fb,W_end,H)