"""Modern Efficient Airplane"""
PAX_max = 240 #Max number of passengers
S_Pmax = 12000 #km, Range at max payload
Ms_mp = 40 #tonne, Maximum payload
Ms_e = 106 #tonne, Empty weight
Ms_fmp = 73 #tonne, Fuel capacity at max payload
Ms_mto = 220 #tonne, Max take-off weight
V_cruise = 256 #m/s, Cruise TAS
M_cruise = 0.85 #Cruise Mach number
h_cruise = 9.5 #km 31000ft Initial cruise altitude
LDratio_cruise = 21 #Cruise L/D
A_wing = 315 #m2 Wing Area
g = 9.8

"""Engine Parameters"""
r = 45 #Overall pressure ratio r=P03/P02
theta = 6 #Turbine entry temperature ratio theta=T04/T02
n_c = 0.9 #Compressor Efficiency
n_t = 0.9 #Turbine Efficiency
FPR = 1.45 #Fan Pressure Ratio
n_f = 0.92 #Fan Efficiency
n_tr = 0.9 #Transfer Efficiency
gamma = 1.4 #Specific heat ratio of air
Rgas = 287 #J/kgK Gas Constant for air
AF_ratio = 15.1 #Stoichiometric air fuel ratio

""""Modelling Constants"""
k = 0.015 #Fuel burn offset (Breguet Range equation)
c_1 = 0.3 #Aircraft weight correlation 1
c_2 = 1.0 #Aircraft weight correlation 2
K_1 = 0.0125 #Parabolic drag law constant 1
K_2 = 0.0446 #Parabolic drag law constant 2

"""Fuels"""
#Kerosense
Sp_vol = 0.124*10**-2 #m3/kg Specific volume
LCV = 42.7*10**3 #kJ/kg calorific value
Stoich_air = 15.1 #kg air/kg fuel Stoichiometric air

"""Flight Chcs"""
sdH = 0.015 #Normalised Descent Distance