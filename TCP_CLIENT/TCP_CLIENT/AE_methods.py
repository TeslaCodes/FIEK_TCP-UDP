#Arber Emini's method
import msvcrt
import time
import array
import os
import time

def Gishti_Shpejte():
    rekordi = 50
    emri = "no-one"
    garuesit=[]
    while True:
        distanca = int(0)
        print("\n--------------------------------------------------------------")
        print('\n\nMire se vini! Shtypni F he J per te levizur!')
        print(' Nje * = 10m')
        print("\n**Resultati me i mire " + str(rekordi) + "s, by: " + emri)
        emri = input("Shkruani emrin ju lutem ")
        garuesit.append(emri)
        print('\nShtyp ENTER per te filluar')
        input()
        print('Gati!!!')
        time.sleep(1)
        print('Start!')
        
        koha_fillestare = time.time()
        while distanca < 50:
                
                g_majte = msvcrt.getch().decode('ASCII')
                if g_majte == 'f':
                        g_djatht= msvcrt.getch().decode('ASCII')
                        if g_djatht == 'j':
                                distanca += 1
                                print('*')
                                if distanca == 25:
                                        print("* Keni arritur ne 25 m")
                                elif distanca  == 50:
                                        print('*')
                                        
        koha_perfundimtare = time.time() - koha_fillestare
        koha_perfundimtare = round(koha_perfundimtare,2)

        
        print('Gara mbaroi')
        print(koha_perfundimtare)
        
        
        if koha_perfundimtare < rekordi:
                print("Ju keni arritur kohen me te shpejt deri tani! ")
                print('\nShtyp ENTER 3 here per te luajtur perseri')
                input() 
                input()
                input()

                
                rekordi = koha_perfundimtare

def TEKSTI():
   
    gjeresia = 90 # gjeresia prej nga fillon te paraqitet teksti(nga djathtas-> majtas)
    mesazhi = "PYTHON!".upper() 
    mesazhiPrintuar = [ "","","","","","","" ]

    
    shkronjat = { " " : [  " ",
                           " ",
                           " ",
                           " ",
                           " ",
                           " ",
                           " " ],

                   "P" : [ "****** ",
                           "*     *",
                           "*     *",
                           "****** ",
                           "*      ",
                           "*      ",
                           "*      " ],
               
                   "Y" : [ "*     *",
                           " *   * ",
                           "  * *  ",
                           "   *   ",
                           "   *   ",
                           "   *   ",
                           "   *   " ], 

                   "T" : [ "*******",
                           "   *   ",
                           "   *   ",
                           "   *   ",
                           "   *   ",
                           "   *   ",
                           "   *   " ],

                   "H" : [ "*     *",
                           "*     *",
                           "*     *",
                           "*******",
                           "*     *",
                           "*     *",
                           "*     *" ],
                    
                   "O" : [" ***** ",
                          "*     *",
                          "*     *",
                          "*     *",
                          "*     *",
                          "*     *",
                          " ***** " ],

                   "N" : ["**    *",
                          "* *   *",
                          "*  *  *",
                          "*   * *",
                          "*    **",
                          "*     *",
                          "*     *" ],

                   "!" : [ "  **  ",
                           "  **  ",
                           "  **  ",
                           "  **  ",
                           "  **  ",
                           "      ",
                           "  **  " ]
               
                   }

    
    # pamja ndertohet rresht per rresht per secilen shkronje fillimisht shtypet rreshti i pare e keshtu me rradhe
    for rreshti in range(7): # pasi qe qdo shkronje paraqitet ne 7 rreshta!
        for karakteri in mesazhi: # per qdo shkronj ne mesazh
            mesazhiPrintuar[rreshti] += (str(shkronjat[karakteri][rreshti]) + "  ")  #karakterin e pare te seciles liste ne shkronjat e vendosim ne listen e strignjeve mesazhiPrintuar

    starti = gjeresia      # gjeresia prej nga fillon te paraqitet teksti(nga djathtas-> majtas)

    while True:
        os.system("cls")
        #printojm secilin karakter te mesazhiPrintuar me nga nje hapsire ne mes
        for rreshti in range(7):
            print(" " * starti + mesazhiPrintuar[rreshti][max(0,starti*-1):gjeresia - starti])
        starti -=1         #e zhvendos mesazhin per 1 karakter majtas

        if starti <= ((len(mesazhi)+2)*6) * -1:         #kur kalon i gjith mesazhi ateher detyroje qe te rifilloj nga ana e djatht ne gjeresi fillestare
            starti = gjeresia

        #time.sleep(0.05)            #shpejtesia e levizjes se tekstit 

                  