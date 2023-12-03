import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

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


nu = 1
s_section = 10 #km
h_array = [7,7.5,8,8.5,9,9.5,10,10.5,11]
h_const = False

if h_const ==True:
   filename = "consth"
else:
   filename = "cclimb"

FPR = RD.FPR
r = RD.r
theta = RD.theta

for i in range(len(h_array)):
  h_start= h_array[i]
  h_start_str = str(h_start)
  W = W_start
  Ms = Ms_start
  Ms_f = Ms_f_start
  
  

  n_cycle = Eng.n_cycle(theta,RD.r,RD.n_t,RD.n_c)
  s_cumulative = 0
  E_co2 = 0.0
  E_nox = 0.0

  #Takeoff ---------------------------
  h = h_start
  Ms_fb = Ms_start * RD.k
  Ms_f = Ms_f - Ms_fb
  W = W - (Ms_fb*RD.g)
  M = LD.Vels(W,h,nu)[0]
  V = LD.Vels(W,h,nu)[1]
  #print(round(s_cumulative),round(Ms_fb,2), round(Ms_f,2) )
  data = {"Dist":[round(s_cumulative,2)],"Alt":[round(h_start,2)],"Mach":[round(M,2)], "TAS":[round(V,2)], \
                "Fuel": [round(Ms_f,2)], "Fuel Burn":[round(Ms_fb,2)]}
  df = pd.DataFrame(data)

  #Cruise Loop -----------------------
  print("Start of Cruise ------")
  while Ms_f > 0:
      WL_KG = LD.Wingloading(W)[1]
      if h_const == True:
        M = LD.Vels(W,h,nu)[0]
      else:
        h = LD.Heights(W,M,nu)

      V = LD.Vels(W,h,nu)[1]

      LD_ratio = LD.LD_ratio(nu)

      n_prop = Eng.n_prop(h,M,FPR)
      n_0 = Eng.n_0(n_prop,n_cycle)

      H = Brg.Breguet(n_0,LD_ratio,W,s_section)[2]
      Ms_fb = Brg.Breguet(n_0,LD_ratio,Ms,s_section)[0]
      Ms_f = Ms_f - Ms_fb
      W = W - (Ms_fb*RD.g)
      s_cumulative = s_cumulative + s_section
      #print(round(s_cumulative), round(Ms_f,2),round(Ms_fb/s_section,2),round(M,2), round(LD_ratio,2), round(n_0,2),round(n_prop,2) )
      
      E_nox = Em.EI_nox(M,h,Ms_fb,r)[0]
      E_co2 = Em.EI_co2(Ms_fb)[0]

      data2 = {"Dist":[s_cumulative],"Alt":[h],"Mach":[M], "TAS":[V], \
                "Fuel": [Ms_f], "Fuel Burn":[Ms_fb], "gNOx":[E_nox],\
                  "gCO2": [E_co2], "n_prop":[n_prop], "n_cycle":[n_cycle],\
                      "n_0":[n_0], "H":[H]}
      df2 = pd.DataFrame(data2)
      df = pd.concat([df, df2],ignore_index = True)
  print(filename+h_start_str)
  #print(df)
  df.to_csv("C:\\Users\\jaket\\Python Projects\\4A7_Aviation_Environment\\Data_Files\\"+filename+h_start_str+".csv",\
            sep=',', index=False, encoding='utf-8')

