import os,time
import pyautogui as pag
try:
    while True:
            print("Press Ctrl-C to end")
            x,y = pag.position() 
            posStr="Position:"+str(x).rjust(4)+','+str(y).rjust(4)
            print (posStr)
            time.sleep(0.2)
            os.system('cls')
except  KeyboardInterrupt:
    print ('end....')