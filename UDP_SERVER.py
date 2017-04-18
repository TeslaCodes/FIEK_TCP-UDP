from socket import *
from metodat import *  #importimi i metodave nga nje fajll.py tjeter
from sys import *
from threading import *

portiServerit = 9000

socketiServerit = socket(AF_INET, SOCK_DGRAM) 

socketiServerit.bind(('', portiServerit))

#socketiServerit.listen()

print("Serveri eshte i gatshem...\n")
        
#def clientThread():
 #   while True:
        

while True:
    kerkesacomplete, adresaKlientit = socketiServerit.recvfrom(1024) 
    k=kerkesacomplete.decode("ASCII")
    #threading._start_new_thread
    if(getsizeof(k)>128):                   #kontrollojm nese kerkesa qe ka arritur nga klienti te jete me e vogel se 128 bajt dhe te mos jete e zbrazet.
        socketiServerit.sendto(str("Kerkesa qe dergohet ne server nuk mund te jete me e madhe se 128 Byte").encode("ASCII"), adresaKlientit)
    elif(k==''):
        socketiServerit.sendto(str("Kerkesa qe dergohet ne server nuk mund te jete e zbrazet").encode("ASCII"), adresaKlientit)
    
    if len(k.split(' ')) == 1:   #kerkesa e cila na vjen nga klienti ndahet ku ka hapsira dhe numerohet ne sa vende eshte ndare
        kerkesa=k 
        parametri=" " 
        opsioni=" " 
    elif (len(k.split(' ')) != 1 and len(k.split(' ')) != 3): 
        kerkesa,parametri=k.split(' ',1)
        opsioni=" "
    elif len(k.split(' '))==3:
        kerkesa,opsioni,parametri=k.split(' ',3)
    
    

    def IP():                                       #metoda e cila na kthen IP adresen e klientit       
        theIP=adresaKlientit[0]
        return theIP

    def PORT():                                     # metoda e cila na kthen PORTin e klientit
        thePort=adresaKlientit[1]
        return thePort
            
    #Kushtezimet ne baze te kerkeses
    if (kerkesa=="IP"):  
        pergjigjja=IP()
        print("Kerkesa e pranuar '" + kerkesa + "' u procesua.")
        socketiServerit.sendto(str("IP adresa e klientit: ").encode("ASCII")+pergjigjja.encode("ASCII"), adresaKlientit)
    
    elif(kerkesa=="KENO"):
        pergjigjja=str(KENO())
        print("Kerkesa e pranuar '" + kerkesa + "' u procesua.")
        socketiServerit.sendto(str("Numrat e rastit te rangut [1,80]: ").encode("ASCII")+pergjigjja.encode("ASCII"), adresaKlientit)
    
    elif(kerkesa=="TIME"):
        pergjigjja=str(TIME())
        print("Kerkesa e pranuar '" + kerkesa + "' u procesua.")
        socketiServerit.sendto(pergjigjja.encode("ASCII"), adresaKlientit)
            
    elif(kerkesa=="PRINTO" and parametri==" "):
       # if(parametri==''):
        pergjigjja="Nuk keni shtypur tekstin qe deshironi ta printoni"
        socketiServerit.sendto(pergjigjja.encode("ASCII"), adresaKlientit)
    elif(kerkesa=='PRINTO' and parametri!=''):

        pergjigjja=str(PRINTO(parametri))
        print("Kerkesa e pranuar '" + kerkesa + "' u procesua.")
        socketiServerit.sendto(pergjigjja.encode("ASCII"), adresaKlientit)
        pergjigjja=''
    
    elif(kerkesa=="ZANORE" and parametri==" "):
        pergjigjja="Nuk keni shtypur tekstin ne te cilin dershironi te numeroni zanoret!"
        socketiServerit.sendto(pergjigjja.encode("ASCII"), adresaKlientit)

    elif(kerkesa=="ZANORE" and parametri!=''):
        pergjigjja=str(ZANORE(parametri))
        print("Kerkesa e pranuar '" + kerkesa + "' u procesua.")
        socketiServerit.sendto(str("Teksti i derguar permbane ").encode("ASCII")+pergjigjja.encode("ASCII")+str(" zanore.").encode("ASCII"), adresaKlientit)

    elif(kerkesa=="FAKTORIEL" and parametri==" "):
        
        pergjigjja="Nuk keni shtypur numrin te cilit deshironi te ja llogaritni faktorielin"          
        socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)
    
    elif(kerkesa=="FAKTORIEL" and parametri!=""):
        pergjigjja=FAKTORIEL(parametri)
        print("Kerkesa e pranuar '" + kerkesa +" u procesua.")            
        socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)

    elif(kerkesa=="HOST"):
        pergjigjja=HOST()
        print("Kerkesa e pranuar '" + kerkesa +" u procesua.")            
        socketiServerit.sendto(str(pergjigjja).encode("ASCII","ignore"), adresaKlientit)
    
    elif(kerkesa=="PORT"):
        pergjigjja=PORT()
        print("Kerkesa e pranuar '" + kerkesa +" u procesua.")            
        socketiServerit.sendto(str(pergjigjja).encode("ASCII","ignore"), adresaKlientit)
    
        
    elif(kerkesa=="KONVERTO" and parametri!='' and opsioni!=''):
    
        if(opsioni=="CelsiusToKelvin"):
            pergjigjja=CelsiusToKelvin(parametri)
            print("Kerkesa e pranuar '" + kerkesa + "' me opsionin "+ opsioni+ " u procesua.")            
            socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)

        elif (opsioni=="CelsiusToFahrenheit"):
            pergjigjja=CelsiusToFahrenheit(parametri)
            print("Kerkesa e pranuar '" + kerkesa + "' me opsionin "+ opsioni+ " u procesua.")            
            socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)


        elif (opsioni=="KelvinToFahrenheit"):
            pergjigjja=KelvinToFahrenheit(parametri)
            print("Kerkesa e pranuar '" + kerkesa + "' me opsionin "+ opsioni+ " u procesua.")            
            socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)


        elif (opsioni=="KelvinToCelsius"):
            pergjigjja=KelvinToCelsius(parametri)
            print("Kerkesa e pranuar '" + kerkesa + "' me opsionin "+ opsioni+ " u procesua.")            
            socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)


        elif (opsioni=="FahrenheitToCelsius"):
            pergjigjja=FahrenheitToCelsius(parametri)
            print("Kerkesa e pranuar '" + kerkesa + "' me opsionin "+ opsioni+ " u procesua.")            
            socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)


        elif (opsioni=="FahrenheitToKelvin"):
            pergjigjja=FahrenheitToKelvin(parametri) 
            print("Kerkesa e pranuar '" + kerkesa + "' me opsionin "+ opsioni+ " u procesua.")            
            socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)


        elif (opsioni=="PoundToKilogram"):
            pergjigjja=PoundToKilogram(parametri)
            print("Kerkesa e pranuar '" + kerkesa + "' me opsionin "+ opsioni+ " u procesua.")            
            socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)


        elif (opsioni=="KilogramToPound"):
            pergjigjja=KilogramToPound(parametri)
            print("Kerkesa e pranuar '" + kerkesa + "' me opsionin "+ opsioni+ " u procesua.")            
            socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)

        elif (kerkesa=="KONVERTO" and parametri==' ' and opsioni==' '):
            pergjigjja="Kerkesa Konverto nuk eshte formuluar si duhet !"        
            socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)

        elif (kerkesa=="KONVERTO" and parametri!='' and opsioni==' '):
            pergjigjja="Nuk keni shtypur temperaturen qe doni ta konvertoni!"        
            socketiServerit.sendto(str(pergjigjja).encode("ASCII"), adresaKlientit)

        #else: socketiServerit.sendto(str("Ky opsion nuk eksiston").encode("ASCII"), adresaKlientit)

           

    else: socketiServerit.sendto(str("Kjo kerkese nuk eshte valide!").encode("ASCII"), adresaKlientit)