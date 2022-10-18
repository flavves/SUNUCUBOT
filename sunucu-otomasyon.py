# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 21:36:42 2022

@author: okmen
"""
# donmadan inşallah lfdkjsdlfksjd
print("basladı")




from pyautogui import locateOnScreen,click,mouseDown,center,mouseUp


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


    
#giriş yap
while 1:
    resim=locateOnScreen('resimler/login.png',confidence=0.93 ,grayscale = True)
    if resim !=None:
        print("buldu")
        korx, kory = center(resim)
        click(x=korx, y=kory)
        mouseDown(); mouseUp() 
        
        resim=locateOnScreen('resimler/executor.png',confidence=0.93 ,grayscale = True)
        if resim !=None:
            print("buldu")
            korx, kory = center(resim)
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
        break

while 1:
    resim=locateOnScreen('resimler/select_file.png',confidence=0.93 ,grayscale = True)
    if resim !=None:
        print("buldu")
        korx, kory = center(resim)
        click(x=korx, y=kory)
        mouseDown(); mouseUp() 
        break














