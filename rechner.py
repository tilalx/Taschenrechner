# Tilo Alexander
# Stand 17.10.2021
# V.1.2


import re
import math
import os
import time

def start():
    print ("#############################################################################################")
    print ("###############################:T A S C H E N R E C H N E R:#################################")
    print ("#############################################################################################")
    print ("######################################:Tilo Alexander:#######################################")
    print ("#############################################################################################")
    print ("#############:     commands:       / help       /clear        /exit      :###################")
    print ("#############################################################################################")
    print ("")

cls = lambda: print('\n'*100)
cls()

start()

while True:
    # Input & character test
    my_string = input("Rechnung Eingeben:")
    if my_string == "/exit":
        print("exiting ....")
        time.sleep(3)
        break
        


    if my_string == "/help":
        cls = lambda: print('\n'*100)
        cls()
        print ("_________________________________Addieren x+x________________________________________")
        print ("________________________________Subrahieren x-x______________________________________")
        print ("_______________________________Multiplizieren x*x____________________________________")
        print ("_________________________________Dividieren x/x______________________________________")
        print ("________________________________Quadratwurzel: √x____________________________________")
        print ("________________________________Klammern x*(x+x)_____________________________________")
        print ("_______Gültige Zeichen: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ., +, -, *, /, (.), √__________")
        continue
        
    if my_string == "/clear":
        cls = lambda: print('\n'*100)
        cls()
        start()
        continue

    if all(x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+", "-", "*", "/", "(", ")", "√"] for x in my_string) is False:
        print("Ungültiges Zeichen wie: Leerzeichen; ^; ; ,;")
        print("____________Für Hilfe: /help________________")
        continue
    # Operation
    try:  
        test1 = re.sub(r"(\d)\(", r"\1*(", my_string)
        test2 = re.sub(r"(\d)√", r"\1*√", test1)
        test3 = re.sub(r"√(\d)", r"math.sqrt(\1)", test2)
        result = eval(test3)
        if str(result)[-2:] == ".0":
            print(int(result))
        else:
            print(result)
    except ZeroDivisionError:
        print("Nicht durch 0 Teilbar")
    except SyntaxError:
        print("Ungültige Eingabe")
