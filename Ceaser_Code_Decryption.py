'''Console Output Sample'''
'''Key: 14'''
'''Decrypted Output: I believe the imagination is the passport that we create to help take us into the real world'''


import numpy as np

text = "W pszwsjs hvs waouwbohwcb wg hvs doggdcfh hvoh ks qfsohs hc vszd hoys ig wbhc hvs fsoz kcfzr"

temp = 0

for j in range(1,27):
    Output = ""
    for i in range(len(text)):
        '''Decryption Needs to go Backwards'''
        if ord(text[i])>=97:
            order = ord(text[i])-j
            if order<97:
                order=order+26
            Output+=chr(order)
        elif ord(text[i]) >= 65:
            order = ord(text[i])-j
            if order<65:
                order=order+26
            Output+=chr(order)
        elif ord(text[i]) == 32:
            Output+=text[i]
    #print(Output)
    Words = Output.split(' ')
    '''Testing the Output with all common English Words. If anything hits, we confirm it is English'''
    for w in Words:
        if (w=="the")|(w=="an")|(w=="and")|(w=="or")|(w=="but")|(w=="of")|(w=="for")|(w=="in")|(w=="to")|(w=="with")|(w=="on")|(w=="from")|(w=="at")|(w=="by")|(w=="it")|(w=="you")|(w=="he")|(w=="she")|(w=="they")|(w=="we")|(w=="his")|(w=="that")|(w=="this")|(w=="not")|(w=="yes")|(w=="is")|(w=="was")|(w=="us")|(w=="help")|(w=="into")|(w=="that")|(w=="this")|(w=="we")|(w=="thus"):
            temp=1
            break
        if (w=="The")|(w=="An")|(w=="And")|(w=="Or")|(w=="But")|(w=="Of")|(w=="For")|(w=="In")|(w=="To")|(w=="With")|(w=="On")|(w=="From")|(w=="At")|(w=="By")|(w=="It")|(w=="You")|(w=="He")|(w=="She")|(w=="They")|(w=="We")|(w=="His")|(w=="That")|(w=="This")|(w=="Not")|(w=="Yes")|(w=="Is")|(w=="Was")|(w=="Us")|(w=="Help")|(w=="Into")|(w=="That")|(w=="This")|(w=="We")|(w=="Thus"):
            temp=0
            break
    
    if temp==1:
        break
    
print('Key: %d' % j)
print("Decrypted Output: %s" % Output)
   
 
