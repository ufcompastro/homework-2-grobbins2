#Altitude of a satellite by Grady Robbins, AST4930

from math import pi

# a) Satellite orbits once every T seconds, altitude above Earth is h = (GMT**2/4pi**2)**1/3 - R

Rkm = 6371 # radius in km, will not be used
R_Earth = Rkm*1000 # radius in m
G = 6.67e-11 # gravitational constant in m**3/kgs**2
M_earth = 5.97e24 # mass in kg

# Program that asks for user's T and prints correct altitude in meters:
T = float(input("The orbital period of this satellite in seconds is: ")) #this asks for T in seconds and converts it to a floating-point value
altitude = ((G*M_earth*(T**2))/(4*(pi**2)))**(1/3) - R_Earth #this is the equation that uses T,G,M, and R to calculate orbit height
print("the altitude of this satellite orbiting Earth is",altitude,"meters")

# b) calculate altitudes orbiting once a day, once every 90 minutes, and once every 45 minutes

T1day = 24*60*60 # orbital period of satellite orbiting once a day using 24 hours to 60 minutes to 60 seconds
T90min = 90*60 # orbital period once every 90 minutes to seconds
T45min = 45*60 # orbital period once every 45 minutes to seconds

def altitude(T): # defining a function for altitude to make readability easier
	altitude = ((G*M_earth*(T**2))/(4*(pi**2)))**(1/3) - R_Earth
	return altitude

print("the altitude of a satellite orbiting once a day is",altitude(T1day),"meters")
print("the altitude of a satellite orbiting once every 90 minutes is",altitude(T90min),"meters")
print("the altitude of a satellite orbiting once every 45 minutes is",altitude(T45min),"meters, which likely means that a satellite cannot have an orbital period of 45 minutes around the Earth.")
