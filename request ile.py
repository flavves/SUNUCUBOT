# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 21:41:28 2022

@author: okmen
"""

import requests
import time
import threading
from pyautogui import locateOnScreen,click,mouseDown,center,mouseUp

global pcadi
with open("resimler/kayit.txt", "r") as dosya:
    veri=dosya.readline()
pcadi=veri.split(",")[0]
apiid=veri.split(",")[1]

#grafik
apiid=apiid

#02129630120

        

global kontrollu_kapatma
kontrollu_kapatma=False
def kapat():
    global kontrollu_kapatma
    kontrollu_kapatma=True
    #ilk açılışta kapatıp tekrar aç
    
    try:
            resim=locateOnScreen('resimler/kapat1.png',confidence=0.93 ,grayscale = True)
            if resim !=None:
                print("buldu")
                korx, kory = center(resim)
                click(x=korx, y=kory)
                mouseDown(); mouseUp() 
                
    except:pass
    
    try:
        resim=locateOnScreen('resimler/kapat2.png',confidence=0.93 ,grayscale = True)
        if resim !=None:
            print("buldu")
            korx, kory = center(resim)
            click(x=korx, y=kory)
            mouseDown(); mouseUp() 
            
    except:pass
    time.sleep(10)
    kontrollu_kapatma=False
 

def baslat():
   
    
    #ilk açılışta kapatıp tekrar aç
    
    try:
            resim=locateOnScreen('resimler/kapat1.png',confidence=0.93 ,grayscale = True)
            if resim !=None:
                print("buldu")
                korx, kory = center(resim)
                click(x=korx, y=kory)
                mouseDown(); mouseUp() 
                
    except:pass
    
    try:
        resim=locateOnScreen('resimler/kapat2.png',confidence=0.93 ,grayscale = True)
        if resim !=None:
            print("buldu")
            korx, kory = center(resim)
            click(x=korx, y=kory)
            mouseDown(); mouseUp() 
            
    except:pass
    
    #8lBoPdzlgkpVDMz
    # pandorayı ara
    while 1:
        resim=locateOnScreen('resimler/pandoraexe.png',confidence=0.93 ,grayscale = True)
        if resim !=None:
            print("buldu")
            korx, kory = center(resim)
            click(x=korx, y=kory)
            mouseDown(); mouseUp() 
            break
    
    
    time.sleep(2)    
    #giriş yap
    while 1:
        resim=locateOnScreen('resimler/login.png',confidence=0.93 ,grayscale = True)
        if resim !=None:
            print("buldu")
            korx, kory = center(resim)
            click(x=korx, y=kory)
            mouseDown(); mouseUp()
            click(x=korx, y=kory)
            mouseDown(); mouseUp()
            click(x=korx, y=kory)
            mouseDown(); mouseUp()
            break
        
    time.sleep(5)
    

    resim=locateOnScreen('resimler/eror_1_Close.png',confidence=0.93 ,grayscale = True)
    if resim !=None:
            print("buldu")
            korx, kory = center(resim)
            click(x=korx, y=kory)
            mouseDown(); mouseUp()
            time.sleep(310)
            while 1:
                resim=locateOnScreen('resimler/login.png',confidence=0.93 ,grayscale = True)
                if resim !=None:
                    print("buldu")
                    korx, kory = center(resim)
                    click(x=korx, y=kory)
                    mouseDown(); mouseUp()
                    click(x=korx, y=kory)
                    mouseDown(); mouseUp()
                    click(x=korx, y=kory)
                    mouseDown(); mouseUp()
                    break
                    
            
    
    while 1:
            
            resim=locateOnScreen('resimler/executor.png',confidence=0.93 ,grayscale = True)
            if resim !=None:
                print("buldu")
                korx, kory = center(resim)
                click(x=korx, y=kory)
                mouseDown(); mouseUp()
                click(x=korx, y=kory)
                mouseDown(); mouseUp() 
                click(x=korx, y=kory)
                mouseDown(); mouseUp() 
                break
    
    
    
    while 1:
        resim=locateOnScreen('resimler/select_file.png',confidence=0.93 ,grayscale = True)
        if resim !=None:
            print("buldu")
            korx_select_file, kory_select_file = center(resim)
            click(x=korx_select_file, y=kory_select_file)
            mouseDown(); mouseUp()
            click(x=korx_select_file, y=kory_select_file)
            mouseDown(); mouseUp() 
            click(x=korx_select_file, y=kory_select_file)
            mouseDown(); mouseUp() 
            break
    # ilk seçeneğe tıkla
    click(x=korx_select_file, y=kory_select_file+20)
    mouseDown(); mouseUp() 
    
    while 1:
        resim=locateOnScreen('resimler/execute.png',confidence=0.93 ,grayscale = True)
        if resim !=None:
            print("buldu")
            korx, kory = center(resim)
            click(x=korx, y=kory)
            mouseDown(); mouseUp() 
            break
    
    click(x=korx_select_file, y=kory_select_file)
    mouseDown(); mouseUp() 
    time.sleep(1)
    click(x=korx_select_file, y=kory_select_file+40)
    mouseDown(); mouseUp() 
    
    while 1:
        resim=locateOnScreen('resimler/execute.png',confidence=0.93 ,grayscale = True)
        if resim !=None:
            print("buldu")
            korx, kory = center(resim)
            click(x=korx, y=kory)
            mouseDown(); mouseUp() 
            break
    while 1:
        resim=locateOnScreen('resimler/main.png',confidence=0.93 ,grayscale = True)
        if resim !=None:
            print("buldu")
            korx, kory = center(resim)
            click(x=korx, y=kory)
            mouseDown(); mouseUp() 
            break
    while 1:
        resim=locateOnScreen('resimler/kucult.png',confidence=0.93 ,grayscale = True)
        if resim !=None:
            print("buldu")
            korx_select_file, kory_select_file = center(resim)
            click(x=korx_select_file, y=kory_select_file)
            mouseDown(); mouseUp() 
            click(x=korx_select_file, y=kory_select_file-50)
            break
        
    time.sleep(3)

    global crashcontrol
    t1 = threading.Thread(target=crashcontrol)
    t1.start()
    
def crashcontrol():
    global kontrollu_kapatma
    time.sleep(5) 
    while 1:
        resim=locateOnScreen('resimler/crashControl.png',confidence=0.93 ,grayscale = True)
        resim2=locateOnScreen('resimler/crashControl2.png',confidence=0.93 ,grayscale = True)
        if ((resim !=None) or (resim2 !=None)):      
            pass
        else:   
            break       
    if kontrollu_kapatma==False:         
            baslat()

            
        




while 1:
    try:    
        time.sleep(4.2)
        response = requests.get("https://api.telegram.org/bot%s/getUpdates?offset=-1"%apiid)
        data = response.json()
        update_id=data["result"][0]["update_id"]
        gelen_mesaj=data["result"][0]["message"]["text"]
        
        
        with open("resimler/gerceklestirilenkodlar.txt", "r") as dosya:
            gerceklestirilenkomutlar=dosya.readline()
        gerceklestirilenkomutlar=gerceklestirilenkomutlar.split("flavvesbatu")
        gerceklestirilenkomutlar.pop(-1)
        #bot burada
        
        if str(update_id) not in gerceklestirilenkomutlar:
            print(gelen_mesaj)
            print(update_id)
            if "/start" in gelen_mesaj:
                    
                mesaj=(gelen_mesaj.replace("/start ",""))
                
                try:
                    if "," in mesaj:
                            
                        mesaj=mesaj.split(",")
                        
                        if pcadi in mesaj:
                            print("%s bota basladı"% pcadi)
                            baslat()
                            
                            with open("resimler/gerceklestirilenkodlar.txt", "a") as dosya:      
                                dosya.write(str(update_id)+"flavvesbatu")
                                
                            time.sleep(5)
                           
                    else:
                    
                        print("tek baslatma geldi")
                        #öncelikle ilk aşamayı kontrol et 0 ise hepsini başlatcan
                        if mesaj=="9999":
                            print("Bütün botlar başladı")
                            baslat()
                            with open("resimler/gerceklestirilenkodlar.txt", "a") as dosya:      
                                dosya.write(str(update_id)+"flavvesbatu")
                            
                        elif mesaj==pcadi:
                            print("%s bota basladı"% pcadi)
                            baslat()
                            with open("resimler/gerceklestirilenkodlar.txt", "a") as dosya:      
                                dosya.write(str(update_id)+"flavvesbatu")
                          
                        else:
                            print("bu session dahil hiçbir şeyi başlatma")
                except:pass
            else:
                #stop işlemleri
                mesaj=(gelen_mesaj.replace("/stop ",""))

                try:
                    if "," in mesaj:
                            
                        mesaj=mesaj.split(",")
                        
                        if pcadi in mesaj:
                            print("%s botu durdu"% pcadi)
                            kapat()
                            with open("resimler/gerceklestirilenkodlar.txt", "a") as dosya:      
                                dosya.write(str(update_id)+"flavvesbatu")
                    else:
                    
                        print("tek durdurma geldi")
                        #öncelikle ilk aşamayı kontrol et 0 ise hepsini başlatcan
                        if mesaj=="9999":
                            print("Hepsi durdu")
                            kapat()
                            with open("resimler/gerceklestirilenkodlar.txt", "a") as dosya:      
                                dosya.write(str(update_id)+"flavvesbatu")
                        elif mesaj==pcadi:
                            print("%s botu durdu"% pcadi)
                            kapat()
                            with open("resimler/gerceklestirilenkodlar.txt", "a") as dosya:      
                                dosya.write(str(update_id)+"flavvesbatu")
                        else:
                            print("bu session dahil hiçbir şeyi durdurma")
                except:pass
                
        
      
        
        
    except:
        time.sleep(10)
















