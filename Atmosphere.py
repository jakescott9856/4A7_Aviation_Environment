import numpy as np
import math
import matplotlib.pyplot as plt
import Reference_Data as RD

global T_sl, P_sl, Ro_sl, a_sl
T_sl = 288.15 #K
P_sl = 101.325 *10**3#Pa
Ro_sl = 1.225 #kg/m3
a_sl = 340.3 #m/s

T_t = 216.65
P_t = P_sl * (T_t/T_sl)**5.256
Ro_t = Ro_sl * (T_t/T_sl)**4.256

def ISA(h):
    if h <= 11:
        T = T_sl - (6.5*h)
        P = P_sl * (T/T_sl)**5.256
        Ro = Ro_sl * (T/T_sl)**4.256

    else:
        float(h)
        T = T_t
        P = P_t * math.exp(-0.1577*(h-11.0))
        Ro = Ro_t * math.exp(-0.1577*(h-11.0))

    a = (math.sqrt(RD.gamma * RD.Rgas * T))
    return(h,T,P,Ro,a)

"""
ISA_hdata = np.linspace(0,20,21)
ISA_Tdata,ISA_Pdata,ISA_Rodata,ISA_adata = ([] for i in range(4))
for i in range(len(ISA_hdata)):
    ISA_Tdata.append(ISA(ISA_hdata[i])[1]/T_sl)
    ISA_Pdata.append(ISA(ISA_hdata[i])[2]/P_sl)
    ISA_Rodata.append(ISA(ISA_hdata[i])[3]/Ro_sl)

plt.plot(ISA_hdata,ISA_Tdata, color = 'k', linestyle = 'solid', label = 'T/T_sl')
plt.plot(ISA_hdata,ISA_Pdata, color = 'b', linestyle = 'dashed', label = 'P/P_sl')
plt.plot(ISA_hdata,ISA_Rodata, color = 'r', linestyle = 'dashdot', label = 'Ro/Ro_sl')


plt.xlabel("h")
plt.grid(color='k', linestyle='-', linewidth=0.1)
plt.legend()
plt.title("ISA")
plt.show()
"""