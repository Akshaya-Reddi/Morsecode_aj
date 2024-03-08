#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import winsound
import re

frequency=1000
dotdur=500
dashdur=1000
pausedur=2000

def beep(dur):
    winsound.Beep(frequency,dur)

def pause(dur):
    time.sleep(dur/1000)

def morse_audio(morsecode):
    for char in morsecode:
        if (char=='.'):
            beep(dotdur)
        elif (char=='-'):
            beep(dashdur)
        elif (char==' '):
            pause(pausedur)
        else:
            print("Something went wrong\nTry again")
            pause(dashdur)

morse={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.---','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'----','?':'..--..','!':'-.-.--','.':'.-.-.-',',':'--..--',';':'-.-.-.',':':'---...','+':'.-.-.','-':'-....-','/':'-..-.','=':'-...-','(':'-.--.',')':'-.--.-','_':'..--.-','@':'.--.-.','&':'.-...','"':'.-..-.','$':'...-..-',"'":'.----.'," ":" "}

def morse_code(string):
    mor_cod=str=""
    for i in string:
        if re.search("[a-z]",string):
            str+=i.upper()
        else:
            str+=i
    try:
        for char in str:
            mor_cod+=morse[char]+" "
        return(mor_cod)
    except KeyError:
        print("The character you mentioned in this message is not found")

def morse_code_rev(mc):
    morse_rev={}
    for i,j in morse.items():
        morse_rev[j]=i
    message=""
    try:
        for char in mc:
            message+=morse_rev[char]
        return(message)
    except KeyError:
        print("The code you entered is not found\nPlease enter carefully")

def morsecode():
    while True:
        flag=0
        while (flag <= 0):
            print("1.Message to Morse code translator\n2.Morse code to message translator")
            ch=input("Select option:")
            if (ch=='1'):
                string=input("Enter message:")
                print("Message:%s\nMorse code:%s"%(string, morse_code(string)))
                morse_audio(morse_code(string))
                print("Completed \U0001F600")
                flag+=1
            elif (ch=='2'):
                print("(Enter code by giving space between each code)")
                mc=[x for x in input("Enter Morse code:").split(' ')]
                mc1=" ".join(mc)
                print("Morse code:%s\nMessage:%s"%(mc1,morse_code_rev(mc)))
                print("The Morse code you entered is:(Listen the sound)")
                morse_audio(mc1)
                print("Completed \U0001F600")
                flag+=1
            else:
                print("Invalid choice\nEnter again")
        rep=input("Do you want to repeat again (yes/no):")
        rep1=rep.lower()
        if (rep1=='yes'):
            print("Request accepted")
        elif (rep1=='no') :
            print("Thank you",end="")
            print("\U0001F600")
            break
        else:
            print("Invalid answer")

morsecode()

