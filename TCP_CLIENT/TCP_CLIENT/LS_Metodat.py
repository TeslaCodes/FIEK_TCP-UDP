#Laureta Svarça
import random #importoje random proceduren ne menyre qe perzgjedhja te jete e paparashikueshme

def GLG(): #metoda GuriLeterGershere --->GLG
    #krijojme nje varg me levizje 
   levizjet=["guri","leter","gershere"]
# krijojm nje lloje unaze (loop forever)
   vazhdo_luaj=true
 #e bejme programin loop duke u bazuar ne switch:
   while vazhdo_luaj=="true":
       levizja_kompjuterit=random.choice(levizjet)#e bejme kompjuterin te zgjedh rastesishem prej vargut larte
       levizja_personit=input("Cfare deshironi te zgjedhni: guri,leter apo gershere")#e lejon personin (lojtarin) te zgjedh vetë
       if levizja_kompjuterit==levizja_personit: #kodi tani i tani e tutje eshte i logjikshem se cfare zgjedhim ne dhe kompjuteri ashtu eshte rezultati!
           print("Barazim")
       elif levizja_personit=="guri" and levizja_kompjuterit=="gershere":
               print("Personi fiton")
       elif levizja_personit=="guri" and levizja_kompjuterit=="leter":
               print("Kompjuteri fiton")
       elif levizja_personit=="leter" and levizja_kompjuterit=="guri":
               print("Personi fiton")
       elif levizja_personit=="leter" and levizja_kompjuterit=="gershere":
               print("Kompjuteri fiton")
       elif levizja_personit=="gershere" and levizja_kompjuterit=="leter":
               print("Personi fiton")
       elif levizja_personit=="gershere" and levizja_kompjuterit=="guri":
               print("Kompjuteri fiton")
               
               
def HoroskopiKinez(): #metoda HoroskopiKinez qe eshte program qe na tregon shenjen tone te horoskopit duke u bazuar ne Horoskop Kinez!
     
   print ("Ky program tregon shenjen tende te horoskopit")
   vitiLindjes=int(input("Ju Lutem jepni vitin e lindjes:")) 
   if vitiLindjes%12==0:
       print("""Shenja juaj e horoskopit eshte Majmun!
       Numri me fat i juaji eshte: 1,7,8 
       Ngjyra qe ju sjell fat:bardhe,ari,kalter""")
   elif vitiLindjes%12==11:
       print("""Shenja juaj e horoskopit eshte Cjap!
       Numri me fat i juaji eshte: 2,7
       Ngjyra qe ju sjell fat:kafte,kuqe,vjollce""")
   elif vitiLindjes%12==10:
       print("""Shenja juaj e horoskopit eshte Kali!
       Numri me fat i juaji eshte:3,4,9
       Ngjyra qe ju sjell fat:gjelbert,kuqe,vjollce""")
   elif vitiLindjes%12==9:
       print("""Shenja juaj e horoskopit eshte Gjarper!
       Numri me fat i juaji eshte: 2,8,5
       Ngjyra qe ju sjell fat:zeze,kuqe,verdhe""")
   elif vitiLindjes%12==8:
         
       print("""Shenja juaj e horoskopit eshte Dragoi!
       Numri me fat i juaji eshte: 1,7,6
       Ngjyra qe ju sjell fat:ari,argjend,hiri""")
   elif vitiLindjes%12==7:
       print("""Shenja juaj e horoskopit eshte Lepur!
       Numri me fat i juaji eshte: 3,4,9
       Ngjyra qe ju sjell fat:kalter,kuqe,pembe""")
   elif vitiLindjes%12==6:
       print("""Shenja juaj e horoskopit eshte Tiger!
       Numri me fat i juaji eshte: 1,3,4
       Ngjyra qe ju sjell fat:kalter,hiri,bardhe,portokallte""")
   elif vitiLindjes%12==5:
       print("""Shenja juaj e horoskopit eshte Demë!
       Numri me fat i juaji eshte: 1,4
       Ngjyra qe ju sjell fat:kalter,verdhe,gjelbert""")
   elif vitiLindjes%12==4:
       print("""Shenja juaj e horoskopit eshte Mi!
       Numri me fat i juaji eshte: 2,3
       Ngjyra qe ju sjell fat:kalter,ari,gjelbert""")
   elif vitiLindjes%12==3:
       print("""Shenja juaj e horoskopit eshte Derr!
       Numri me fat i juaji eshte: 2,5,8
       Ngjyra qe ju sjell fat:verdhe,hiri,kafte,ari""")

   elif vitiLindjes%12==2:
       print("""Shenja juaj e horoskopit eshte Qen!
       Numri me fat i juaji eshte: 3,4,8
       Ngjyra qe ju sjell fat:gjelbert,kuqe,vjollce""")
   elif vitiLindjes%12==1:
       print("""Shenja juaj e horoskopit eshte Gjelë!
       Numri me fat i juaji eshte: 5,7,8
       Ngjyra qe ju sjell fat:kafte,ari,verdhe""")

   else:
           print("Nuk kam kuptuar çka keni dashur te thoni.Ju Lutem shkruani nje numer valid.")
           
  
           

