import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd

import Reference_Data as RD

Datafields = ["S","Alt","M","TAS","Fuel","Fuel Burn", "gNOx", "gCO2", "n prop", "n cycle", "n 0", "H"]
tableau_colors = list(mcolors.TABLEAU_COLORS.values())



t_array = np.linspace(4,8,9)
filename = "t"
t_data = []
for i in range(len(t_array)):
    t = t_array[i]
    t_str = str(t_array[i])
    data = pd.read_csv("C:\\Users\\jaket\\Python Projects\\4A7_Aviation_Environment\\Data_Files\\"+filename+t_str+".csv")
    #print(data)
    S = data.iloc[1:,0].to_numpy()
    Alt = data.iloc[1:,1].to_numpy()
    M = data.iloc[1:,2].to_numpy()
    TAS = data.iloc[1:,3].to_numpy()
    Fuel = data.iloc[1:,4].to_numpy()
    Fuel_Burn = data.iloc[1:,5].to_numpy()
    gNOx = data.iloc[1:,6].to_numpy()
    gCO2 = data.iloc[1:,7].to_numpy()
    n_prop = data.iloc[1:,8].to_numpy()
    n_cycle = data.iloc[1:,9].to_numpy()
    n_0 = data.iloc[1:,10].to_numpy()
    H = data.iloc[1:,11].to_numpy()

    H_avg = sum(H)/len(H)
    NOx_total = sum(gNOx)
    CO2_total = sum(gCO2)
    NOx_passkm = NOx_total/(max(S)*RD.PAX_max)
    CO2_passkm = CO2_total/(max(S)*RD.PAX_max)
    FBPR = max(Fuel)/(max(S)*RD.Ms_mp)
    ND_FBPR = FBPR*H_avg/1000
    ND_Dist = max(S)/H_avg
    n_prop_av = sum(n_prop)/len(n_prop)
    n_cycle_av = sum(n_cycle)/len(n_cycle)
    t_data.append([max(S),NOx_passkm, CO2_passkm, FBPR, ND_FBPR, ND_Dist,n_prop_av,n_cycle_av])
    
    #plt.plot(FPR,n_prop,color = tableau_colors[i], label = FPR_str )


values1 = [sublist[2] for sublist in t_data]/t_data[5][2] #non dim
values2 = [sublist[1] for sublist in t_data]/t_data[5][1]
print(values2)
print()
plt.scatter(t_array,values1,color = tableau_colors[2], label = "Nondim CO2 \n per pass-km")
plt.plot(t_array,values1,color = tableau_colors[2])
plt.scatter(t_array,values2,color = tableau_colors[3], label = "Nondim NOx \n per pass-km")
#plt.plot(t_array,values2,color = tableau_colors[3])

plt.title('Effect of theta ')
plt.xlabel("theta")
plt.ylabel("")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

