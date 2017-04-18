from socket import *
from builtins import *
from AE_methods import *
from LS_Metodat import *
from BG_Metodat import *

serveri = "10.20.35.193"
porti = 9000

socketiKlientit = socket(AF_INET,SOCK_DGRAM)
while True:
    kerkesa = input("Kerkesa:")
    if(kerkesa=='Gishti_Shpejte'):
        print(Gishti_Shpejte())
    elif(kerkesa=='TEKSTI'):
        print(TEKSTI())
    elif(kerkesa=="GLG"):
        print(GLG())
    elif(kerkesa=="HoroskopiKinez"):
        print(HoroskopiKinez())
    elif(kerkesa=="SHUMA"):
        print(SHUMA())
    elif(kerkesa=="BashkoFjalet"):
        print(BashkoFjalet())
    else:
        socketiKlientit.sendto(kerkesa.encode("ASCII"),(serveri,porti))

    pergjigjja, serverAddress = socketiKlientit.recvfrom(1024)

    print(pergjigjja.decode("ASCII"))