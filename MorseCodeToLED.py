#ちょっと汚いですが
#python3, Raspi3でうごきます。

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
morseAlphabet ={
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        " " : "/",
        "." : ".-.-.-",
        "," : "--..--",
        ":" : "---...",
        "?" : "..--..",
        "'" : ".----.",
        "-" : "-....-",
        "/" : "-..-.",
        "@" : ".--.-.",
        "=" : "-...-",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----"
        }



def encodeToMorse_and_LED_lightup(message):
        encodedMessage = ""
        for char in message[:]:
            encodedMessage += morseAlphabet[char.upper()] + " "       
        print(encodedMessage)
        
        for _ in list(encodedMessage):
           if _ == ".":
               GPIO.output(25, GPIO.HIGH)
               time.sleep(0.1)
            
               GPIO.output(25, GPIO.LOW)
               time.sleep(0.1)
       
           elif _ == "-":
               GPIO.output(25, GPIO.HIGH)
               time.sleep(0.3)
            
               GPIO.output(25, GPIO.LOW)
               time.sleep(0.1)
            
           else:
               GPIO.output(25, GPIO.LOW)
               time.sleep(0.6)
        GPIO.cleanup()
        
#LED点灯用です。GPIO番号25番を使ってます。

try:
    Message = input("please input: ")
    encodeToMorse_and_LED_lightup(Message)
    
    
except:
    print("Sorry,Please input English.")


