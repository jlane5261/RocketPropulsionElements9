#!/usr/bin python3

"""
This example problem is simply to try and convey some of the equations this chapter introduces.
Super easy plug and chug
"""

#Problem as stated:
# A rocket projectile has the following characteristics:
# Initial mass                               200 kg
# Payload, nonpropulsive structure, etc.     110 kg
# Mass after rocket operation                130 kg
# Rocket operating duration                  3.0 seconds
# Average specific impulse of propellant     240 seconds
# 
# Determine the following: 
# Mass Ratio for the vehicle and propulsive unit
# propellant mass fraction for the vehicle and propulsive unit
# The effective exhaust velocity (c)
# the Total Impulse (I_t)
# 
# If maximum acceleration cannot exceed 35 gs, does this flight exceed max g? 
# 

import time

# Define constants

m_o     = 200 #(kg)
m_veh   = 130 #(kg)
m_non   = 110 #(kg)
dur     = 3 #(seconds)
I_s     = 240 #(seconds)

#order of solving: get MR and Mass Fractions -> then get (c), then get flowrate (m_dot), then get Thrust (T), then get total impulse (I_t), then get Acceleration (F=ma)

# Mass Ratios
print('Calculating Mass Fractions','.','.','.')
time.sleep(0.5)
MR_Veh = m_veh / m_o
print("The Mass Ratio of the Rocket is: -------- ", int(MR_Veh*100),"%")
time.sleep(0.3)
MR_non = (m_veh - m_non) / (m_o - m_non)
print("The Mass Ratio of the Propuslive unit is: ", int((MR_non)*100),"%")
time.sleep(0.2)

#Mass Fractions
print('Now, Calcuation Mass Fractions . . .')
time.sleep(0.6)
m_p = m_o-m_veh
print('Propellant mass is ',(m_p),' kg')
MassFrac_veh = m_p / m_o
print('Propellant mass fraction to the rocket is: -------- ', int(MassFrac_veh * 100), '%')
time.sleep(0.3)
MassFrac_prop = m_p / m_non
print('Propellant mass fraction to the propulsion unit is: ', int(MassFrac_prop*100), '%')
time.sleep(0.2)


# Get c "Effective Exhaust Velocity of the flow"
# c = I_s*g_o
g_o = 9.81 #(m/s^2)
c = I_s * g_o
print('Effective Exhaust Velocity (c) =', float(c), ' m/s')
time.sleep(0.4)


# Get Mass Flowrate and Then Thrust
m_dot = m_p / dur
print('Mass Flowrate = ', float(m_dot), ' kg/sec')
Thrust = c * m_dot
time.sleep(0.4)
print('Thrust = ', Thrust, 'kg*m/sec^2 (N)')

#Get total impulse
I_t = Thrust * dur
print('Total impulse = ', I_t, ' unsure of units')

#Find the total G force (F= ma)
largest_g = Thrust/m_veh
time.sleep(1)
print('Largest G Force experienced in this problem occurs at the end of the thrust profile')
print('Largest G Force = ', largest_g, ' m/sec^2')



time.sleep(2)
print('.')
time.sleep(2)
print('End Example Problem 2-1')