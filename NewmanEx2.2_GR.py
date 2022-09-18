#Altitude of a satellite
from math import pi
# Satellite orbits once every T seconds, altitude above Earth is h = (GMT**2/4pi**2)**1/3 - R
Rkm = 6371 # radius in km, will not be used
R_Earth = Rkm*1000 # radius in m
G = 6.67e-11 # gravitational constant in m**3/kgs**2
M_earth = 5.97e24 # mass in kg
# Program that asks for user's T and prints correct altitude in meters:
T = float(input("The orbital period of the satellite in seconds is: ")) #this asks for T in seconds and converts it to a floating-point value
altitude = (G*M_earth*T**2/(4*pi**2))**1/3 - R_Earth #this is the equation that uses T,G,M, and R to calculate orbit height
print("the altitude of the satellite orbiting Earth is",altitude,"meters")

