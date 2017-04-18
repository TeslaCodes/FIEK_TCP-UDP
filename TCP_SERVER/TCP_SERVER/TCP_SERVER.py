import socket
import random
import time
import datetime
print ('Duke pritur lidhje...')
host = '127.0.0.1'
port = 9000
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
time1=time.time()
print ('IP adresa dhe porti: ', addr)
while True:
    edhena = conn.recv(BUFFER_SIZE).decode('utf-8')
    kerkesa = edhena.split(' ', 1)[0]
    if not kerkesa: break
    try:
        detyra = edhena.split(' ', 1)[1]
    except IndexError:
        detyra = ''
    try:    
        zgjedh = detyra.split(' ', 1)[0]
    except IndexError:
        zgjedh = ''
    try:
        numri = detyra.split(' ', 1)[1]
    except IndexError:
        numri = ''
    if (kerkesa=="KONVERTO"):
        if numri == '':
            conn.send("Kerkesa duhet te jete e tille : KONVERTO NjesiaToNjesia Vlera, psh: KONVERTO KelvinToCelsius 50".encode('utf-8'))
        else:
            if (zgjedh=="CelsiusToKelvin"):
                tempKelvin=float(numri)+273.15
                conn.send(str(str(numri)+" Celsius eshte "+ str(tempKelvin)+" Kelvin").encode('utf-8'))
            elif (zgjedh=="CelsiusToFahrenheit"):
                tempFahrenheit=(9*float(numri)/5)+32
                conn.send(str(str(numri)+" Celsius eshte "+ str(tempFahrenheit)+" Farenheit").encode('utf-8'))
            elif (zgjedh=="KelvinToFarenheit"):
                tempFahrenheit=1.8*(float(numri)-273)+32
                conn.send(str(str(numri)+" Kelvin eshte "+ str(tempFahrenheit)+" Farenheit").encode('utf-8'))
            elif (zgjedh=="KelvinToCelsius"):
                tempCelsius=float(numri)-273.15
                conn.send(str(str(numri)+" Kelvin eshte "+ str(tempCelsius)+" Celsius").encode('utf-8'))
            elif (zgjedh=="FahrenheitToCelsius"):
                tempCelsius=5*(float(numri)-32)/9
                conn.send(str(str(numri)+" Fahrenheit eshte "+ str(tempCelisus)+" Celsius").encode('utf-8'))
            elif (zgjedh=="FahrenheitToKelvin"):
                tempCelsius=5*(float(numri)-32)/9
                tempKelvin=tempCelsius+273.15
                conn.send(str(str(numri)+" Fahrenheit eshte "+ str(tempKelvin)+" Kelvin").encode('utf-8'))
            elif (zgjedh=="PoundToKilogram"):
                Kilogram=float(numri)*0.45359237
                conn.send(str(str(numri)+" Pound eshte "+ str(Kilogram)+" Kilogram").encode('utf-8'))
            elif (zgjedh=="KilogramToPound"):
                Pound=float(numri)*2.2046226218
                conn.send(str(str(numri)+" Kilogram eshte "+ str(Pound)+" Pound").encode('utf-8'))
            else:
                conn.send("Kerkesa duhet te jete e tille: KONVERTO NjesiaToNjesia> Vlera, psh: KONVERTO KelvinToCelsius 50".encode('utf-8'))
    elif (kerkesa=="ZANORE"):
        count = 0
        zanore = ['a', 'e', '?', 'i', 'o', 'u', 'y']
        detyra=detyra.lower()
        for char in detyra:
            if char in zanore:
                count += 1
        conn.send(str("Ketu ka "+str(count)+" zanore.").encode('utf-8'))
    elif (kerkesa=="IP"):
        conn.send(str("IP-ja e juaj eshte "+str(addr[0])).encode('utf-8'))
    
    elif (kerkesa=="HOST"):
        if socket.gethostname()=='':
            conn.send("Nuk ka host te tille".encode('utf-8'))
        else: 
            hostname=socket.gethostname()
            conn.send((hostname).encode('utf-8'))
    elif (kerkesa=="PORT"):
        conn.send(str("Porti juaj eshte "+str(addr[1])).encode('utf-8'))
    elif (kerkesa=="PRINTO"):
        if detyra=='':
            conn.send("Ju nuk keni shkruajtur asgje".encode('utf-8'))
        else:
            conn.send(str("Ju keni shkruar: " + str(detyra)).encode('utf-8'))
    elif (kerkesa=="FAKTORIEL"):
        if detyra == '':
            conn.send("Kerkesa duhet te jete e tille: FAKTORIEL numri psh: FAKTORIEL 5".encode('utf-8'))
        else:
            nr=float(zgjedh)
            if nr < 0:
                conn.send("Nuk ekziston faktorieli per numrat negative".encode('utf-8')) 
            elif nr == 0:
                conn.send("Faktorieli i numrit 0 eshte 1".encode('utf-8'))
            elif nr > 1:
                faktoriel=1
                while nr>1:
                    faktoriel=faktoriel*nr
                    nr=nr-1
                conn.send(str("Faktorieli i numrit "+ zgjedh +" eshte "+ str(faktoriel)).encode('utf-8'))
    elif (kerkesa=="KENO"):
        Random=[random.randint(1,80) for i in range(20)]
        conn.send(str(Random).encode('utf-8'))
    elif (kerkesa=="TIME"):
        Time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn.send(str(Time).encode('utf-8'))
#    elif (kerkesa=="SHUMA"):
       # if zgjedh=='' or numri=='':
        #    conn.send("Per te gjetur shumen e dy numrave, shkruani SHUMA numri1 numri2".encode('utf-8'))
        #else:
         #   try:
          #      numri1=float(zgjedh)
           #     numri2=float(numri)
            #    conn.send(str("Shuma e ketyre numrave eshte "+str(numri1+numri2)).encode('utf-8'))
            #except ValueError:
             #   conn.send("Per te gjetur shumen e dy numrave, shkruani SHUMA numri1 numri2".encode('utf-8'))
        conn.send(edhena.encode('utf-8'))
    #elif(kerkesa=="BASHKOFJALET"):
     #  if zgjedh=='' or numri=='':
      #      conn.send("Per te bashkuar dy fjale, shkruani BASHKOFJALET fjala1 fjala2".encode('utf-8'))
       #else:
        #    try:
         #       fjala1=str(zgjedh)
          #      fjala2=str(numri)
           ##except ValueError:
             #   conn.send("Per te bashkuar dy fjale, shkruani BASHKOFJALET fjala1 fjala2".encode('utf-8'))  
           
  
conn.close()