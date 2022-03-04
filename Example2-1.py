#!/usr/bin python3

"""
This example problem is simply to try and convey some of the equations this chapter introduces.
Super easy plug and chug
"""

#Problem as stated:
# A rocket projectile has the following characteristics:
# Initial mass                               200 kg
# Mass after rocket operation                130 kg
# Payload, nonpropulsive structure, etc.     110 kg
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


# Define constants

m_o     = 200 #(kg)
m_veh   = 130 #(kg)
m_non   = 110 #(kg)
dur     = 3 #(seconds)
I_s     = 240 #(seconds)

#order of solving: get MR and Mass Fractions -> then get (c), then get flowrate (m_dot), then get Thrust (T), then get total impulse (I_t), then get Acceleration (F=ma)

