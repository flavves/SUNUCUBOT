# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 09:47:14 2022

@author: okmen
"""
global pcadi
with open("resimler/kayit.txt", "r") as dosya:
    veri=dosya.readline()
pcadi=veri.split(",")[0]
apiid=veri.split(",")[1]

#grafik
apiid=apiid

import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time
from pyautogui import locateOnScreen,click,mouseDown,center,mouseUp
import threading

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

logger = logging.getLogger(__name__)


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
            bot = telegram.Bot(apiid)
        
            bot.send_message(-602463761,("%s botu durdu pandora programının tekrar başlatılmaya ihtiyacı var"% pcadi))
            break
        
    if kontrollu_kapatma==False:
            bot = telegram.Bot(apiid)
            
            bot.send_message(-602463761,("%s botu hata aldı tekrar baslatılıyor"% pcadi))
            baslat()
            bot.send_message(-602463761,("%s botu hata aldı tekrar başlatıldı"% pcadi))
            
        
    

def start(update, context):
    print("mesaj geldi")
    try:
        gelen_mesaj=update["message"]["text"]
        chatid=update["message"]["chat"]["id"]
        print(chatid)
    except Exception as e:
        gelen_mesaj="yokflavves"
        print("hata mesajı",e)
    
    
    #bot = telegram.Bot(apiid)
    #bot.send_photo(str(chatid), "https://www.tradingview.com/x/mBrakyg2/")
    mesaj=(gelen_mesaj.replace("/start ",""))
    
    
    update.message.reply_text(chatid)
    update.message.reply_text(mesaj)
    
    
    
    
    try:
        if "," in mesaj:
                
            mesaj=mesaj.split(",")
            
            if pcadi in mesaj:
                update.message.reply_text("%s bota basladı"% pcadi)
                baslat()
                time.sleep(5)
               
        else:
        
            print("tek baslatma geldi")
            #öncelikle ilk aşamayı kontrol et 0 ise hepsini başlatcan
            if mesaj=="9999":
                update.message.reply_text("Bütün botlar başladı")
                baslat()
                
            elif mesaj==pcadi:
                update.message.reply_text("%s bota basladı"% pcadi)
                baslat()
              
            else:
                print("bu session dahil hiçbir şeyi başlatma")
    except:pass
        
        
def stop(update, context):
    print("mesaj geldi")
    try:
        gelen_mesaj=update["message"]["text"]
        chatid=update["message"]["chat"]["id"]
        print(chatid)
    except Exception as e:
        gelen_mesaj="yokflavves"
        print("hata mesajı",e)
    
   
    #bot = telegram.Bot(apiid)
    #bot.send_photo(str(chatid), "https://www.tradingview.com/x/mBrakyg2/")
    mesaj=(gelen_mesaj.replace("/stop ",""))
    
    
    #update.message.reply_text(chatid)
    #update.message.reply_text(mesaj)
       
    #print(mesaj)
    try:
        if "," in mesaj:
                
            mesaj=mesaj.split(",")
            
            if pcadi in mesaj:
                update.message.reply_text("%s botu durdu"% pcadi)
                kapat()
        else:
        
            print("tek durdurma geldi")
            #öncelikle ilk aşamayı kontrol et 0 ise hepsini başlatcan
            if mesaj=="9999":
                update.message.reply_text("Hepsi durdu")
                kapat()
            elif mesaj==pcadi:
                update.message.reply_text("%s botu durdu"% pcadi)
                kapat()
            else:
                print("bu session dahil hiçbir şeyi durdurma")
    except:pass
  
        
    


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Yardım geliyor')
    

def echo(update, context):
    #update.send_photo("https://www.tradingview.com/x/uXYt44GD/")
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    bot = telegram.Bot(apiid)

    bot.send_message(-602463761,("%s botu hata aldı"% pcadi))


def main():

    token = apiid
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    #komutlar burada
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("help", help))

    dp.add_error_handler(error)
    
    
    
    
    
    
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()























