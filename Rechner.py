# @tilalx
# Stand 17.10.2021
# V.1.3

import re
import math
import os
import time
from datetime import date
import socket
import urllib.request
import urllib
from urllib.request import urlopen
from datetime import datetime
import logging
from string import Template
import shutil
import datetime
from pathlib import Path

#rename .log file by create time
directory = './'
extensions = (['.log']);
filelist = os.listdir( directory )
newfilesDictionary = {}
count = 0

for file in filelist:
	filename, extension = os.path.splitext(file)
	if ( extension in extensions ):
		create_time = os.path.getctime( file )
		format_time = datetime.datetime.fromtimestamp( create_time )
		format_time_string = format_time.strftime("%Y-%m-%d %H.%M.%S")
		newfile = format_time_string + extension; 
		if ( newfile in newfilesDictionary.keys() ):
			index = newfilesDictionary[newfile] + 1;
			newfilesDictionary[newfile] = index; 
			newfile = format_time_string + '-' + str(index) + extension;
		else:
			newfilesDictionary[newfile] = 0; 
		os.rename( file, newfile );
		count = count + 1

path = Path('logs')
path.mkdir(parents=True, exist_ok=True)

#move all logs to 'logs'
#aktuelles verzeichnis
wd = os.getcwd()
newPath = os.path.join('logs')

#find data by .log and move it to logs
sourcepath= wd
sourcefiles = os.listdir(sourcepath)
destinationpath = newPath
for file in sourcefiles:
    if file.endswith('.log'):
        shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))

#create new .log data
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='logging.log', encoding='utf-8', level=logging.DEBUG)



#find & show local ipadress & log ip
def check_in():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print("Local Ip: " + s.getsockname()[0])
        logging.debug('')
        logging.debug("Local ip")
        logging.debug(s.getsockname()[0])
        s.close()
    except Exception:
        pass

#time
today = date.today()
d2 = today.strftime("%B %d, %Y")

#start screen
def start():
    print("#############################################################################################")
    print("##############################: T A S C H E N R E C H N E R :################################")
    print("#############################################################################################")
    print("####################################:    til.alx     :#######################################")
    print("#############################################################################################")
    print("#############:     commands:       / help       /clear        /exit      :###################")
    print("#############################################################################################")
    print("####################################",d2,'#######################################')
    print("#############################################################################################")


#clear
def clear():
    cls = lambda: print('\n'*100)
    cls()



#start && show local ip
start()
check_in()

#show an log ip adress

try:
    with urlopen("https://icanhazip.com/robots.txt") as stream:
        logging.debug("External ip")
        logging.debug(stream.read().decode("utf-8"))

    with urlopen("https://icanhazip.com/robots.txt") as ip:
        print('External Ip: ' + ip.read().decode("utf-8"))
except Exception:
    pass



while True:
    # Tet der Eingaben
    my_string = input("Rechnung Eingeben:")
    #/Exit with Question
    if my_string == "/exit":
        question = input("Willst du wirklich beenden (y) or (n):")
        if question == "y":
            print("Closing ....")
            time.sleep(3)
            break
        
        if question == "n":
            clear()
        continue

    #/help
    if my_string == "/help":
        clear()
        print ("_________________________________Addieren x+x________________________________________")
        print ("________________________________Subrahieren x-x______________________________________")
        print ("_______________________________Multiplizieren x*x____________________________________")
        print ("_________________________________Dividieren x/x______________________________________")
        print ("________________________________Quadratwurzel: √x____________________________________")
        print ("________________________________Klammern x*(x+x)_____________________________________")
        print ("_______Gültige Zeichen: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ., +, -, *, /, (.), √__________")
        continue
        
    #/clear mit start screen    
    if my_string == "/clear":
        clear()
        start()
        continue
    
    #Gültige eingaben Test mit evtl Fehlermeldung
    if all(x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+", "-", "*", "/", "(", ")", "√"] for x in my_string) is False:
        print("Ungültiges Zeichen wie: Leerzeichen; ^; ; ,;")
        print("____________Für Hilfe: /help________________")
        continue
    #Ausrechnung
    try:  
        tst1 = re.sub(r"(\d)\(", r"\1*(", my_string)
        tst2 = re.sub(r"(\d)√", r"\1*√", tst1)
        tst3 = re.sub(r"√(\d)", r"math.sqrt(\1)", tst2)
        result = eval(tst3)
        if str(result)[-2:] == ".0":
            logging.debug(int(result))
            print(int(result))
            
        else:
            logging.debug(result)
            print(result)
            logging.debug('result')
            logging.debug(result)
    #Zero division Error
    except ZeroDivisionError:
        print("Nicht durch 0 Teilbar")
    #Syntax Error
    except SyntaxError:
        print("Ungültige Eingabe")
