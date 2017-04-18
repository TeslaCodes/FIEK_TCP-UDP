import socket
from AE_methods import *
from LS_Metodat import *
from BG_Metodat import *
host = '10.20.0.97'
port = 9000
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Shtypni njeren nga kerkesat: \nIP\nPORT\nZANORE\nPRINTO\nHOST\nTIME\nKENO\nKONVERTO\nFAKTORIEL\nSHUMA\nBashkoFjalet")
    
while True:
    edhena = input("---> ")
    if edhena == "":
        print("Ju lutem shtypni njeren nga kerkesat me larte")
    elif edhena=="SHUMA":
        print=SHUMA()
    elif edhena=="BashkoFjalet":
        print(BashkoFjalet())
    elif edhena=="TEKSTI":
        print(TEKSTI())
    elif edhena=="Gishti_Shpejte":
        print(Gishti_Shpejte())
    elif edhena=="HoroskopiKinez":
        print(HoroskopiKinez())
    elif edhena=="GLG":
        print(GLG())
    
        
    else:
        s.send(edhena.encode('utf-8'))
        data=s.recv(BUFFER_SIZE).decode('utf-8')
        print(data)
s.close()