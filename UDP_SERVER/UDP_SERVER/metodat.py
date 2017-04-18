from socket import *
from builtins import print, str
from random import *
from array import *
from datetime import *
from math import *
import msvcrt
import time




def IP():
    theIP=gethostbyname(gethostname())
    return theIP

def HOST():
    theHOST=gethostname()
    return theHOST

def PORT(porti):
    
    return porti[1]

def KENO():
    vargu=[]
    count=0
    while (count<=20):
        nr=randint(1,80)
        vargu.append(nr)
        count=count+1
    return vargu

def TIME():
    time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return time

def PRINTO(teksti):

    return teksti

def ZANORE(teksti):
   nrZanoreve=0
    
   for shkronja in teksti:
       if shkronja in "aeiouAEIOU":
          nrZanoreve=nrZanoreve+1
   return nrZanoreve

def CelsiusToKelvin(celsius):
    kelvin=(float(celsius)+273.15)
    return kelvin

def CelsiusToFahrenheit(celsius):
    fahrenheit=(float(celsius)*9/5.0)+32
    return fahrenheit

def KelvinToFahrenheit(kelvin):
    fahrenheit=(float(kelvin)*9/5.0)-459.67
    return fahrenheit

def KelvinToCelsius(kelvin):
    celsius=(float(kelvin)-273.15)
    return celsius

def FahrenheitToCelsius(fahrenheit):
    celsius= (float(fahrenheit)-32)*5.0/9
    return celsius
    
def FahrenheitToKelvin(fahrenheit):
    kelvin=(float(fahrenheit)+459.67)*5.0/9
    return kelvin
    
def PoundToKilogram(paund):
    kilogram=float(paund)/2.2
    return kilogram
   
def KilogramToPound(kilogram):
    
    paund=float(kilogram)*2.2
    return paund

def FAKTORIEL(n):
    numri=int(n)
    if numri == 0:
        return 1
    else:
        return numri * FAKTORIEL(numri-1)    