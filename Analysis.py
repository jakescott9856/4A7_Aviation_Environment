import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd

import Reference_Data as RD

Datafields = ["S","Alt","M","TAS","Fuel","Fuel Burn", "gNOx", "gCO2", "n prop", "n cycle", "n 0", "H"]
tableau_colors = list(mcolors.TABLEAU_COLORS.values())


boolean_values = [False]
h_array = [7,7.5,8,8.5,9,9.5,10,10.5,11]

for h_const in boolean_values:

    if h_const == True:
        flight_traj = "consth"
        consth_data = []
    else:
        flight_traj = "cclimb"
        cclimb_data = []

    for i in range(len(h_array)):
        h_start_str = str(h_array[i])
        data = pd.read_csv("C:\\Users\\*removed for blind marking*\\Python Projects\\4A7_Aviation_Environment\\Data_Files\\"+flight_traj+h_start_str+".csv")
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

        #print(max(S),NOx_passkm, CO2_passkm, FBPR, ND_FBPR, ND_Dist)
        if h_const == True:
            consth_data.append([max(S),NOx_passkm, CO2_passkm, FBPR, ND_FBPR, ND_Dist])
        else:
            cclimb_data.append([max(S),NOx_passkm, CO2_passkm, FBPR, ND_FBPR, ND_Dist])

        plt.plot(S,gCO2/10,color = tableau_colors[i], label = h_start_str +"km")
#print(consth_data)
#print(consth_data[:][0])
"""
values1 = [sublist[3] for sublist in consth_data]
values2 = [sublist[3] for sublist in cclimb_data]
print(values1)

plt.scatter(h_array,values1,color = "b", label = "Constant Altitude")
plt.plot(h_array,values1,color = "b")
plt.scatter(h_array,values2,color = "r", label = "Cruise Climb")
plt.plot(h_array,values2,color = "r")
"""
plt.title('CO2 emission rate, Constant Altitude')
plt.xlabel("Distance S (km)")
plt.ylabel("CO2 emission rate (gNOx/km)")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()

