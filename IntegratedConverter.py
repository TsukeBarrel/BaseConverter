#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ConvDtB(EntryValue):
    #10進数から2進数へ変換
    Dec = int(EntryValue)
    Rem = 0
    Res = []
    
    while not(Dec == 1):
        Rem = Dec%2
        Res.insert(0, Rem)  
        Dec = Dec//2

    Res.insert(0, Dec)
    return ''.join(map(str, Res))



def ConvBtD(EntryValue):
    #2進数から10進数へ変換
    Bin = list(EntryValue)
    Res = 0
    
    while len(Bin) > 0:
        if int(Bin[0]) == 1:
            Res += 2**(len(Bin)-1)
            Bin.pop(0)
    
        else:
            Bin.pop(0)
    
    return str(Res)
    
    
    
def ConvDtH(EntryValue):
    #10進数から16進数へ変換
    Dec = int(EntryValue)
    Rem = 0
    Res = []
    
    while not(Dec == 0):
        Rem = Dec%16
    
        if Rem == 10:
            Res.insert(0, "A")
        elif Rem == 11:
            Res.insert(0, "B")
        elif Rem == 12:
            Res.insert(0, "C")
        elif Rem == 13:
            Res.insert(0, "D")
        elif Rem == 14:
            Res.insert(0, "E")
        elif Rem == 15:
            Res.insert(0, "F")
        else:
            Res.insert(0, Rem)
        
        Dec = Dec//16

    return ''.join(map(str,Res))


    
def ConvHtD(EntryValue):
    #16進数から10進数へ変換
    Hex = list(EntryValue)
    Tmp, Res = 0, 0

    while len(Hex) > 0:
        if not Hex[0] == "0":
            if Hex[0] == "A":
                Tmp = 10
            elif Hex[0] == "B":
                Tmp = 11
            elif Hex[0] == "C":
                Tmp = 12
            elif Hex[0] == "D":
                Tmp = 13
            elif Hex[0] == "E":
                Tmp = 14
            elif Hex[0] == "F":
                Tmp = 15
            else:
                Tmp = int(Hex[0])
            
            Res += 16**(len(Hex)-1)*Tmp
            Hex.pop(0)
    
        else:
            Hex.pop(0)
    
    return str(Res)



def ConvBtH(EntryValue):
    #2進数から16進数へ変換
    Bin = EntryValue
    Res = ""
    
    Res = ConvDtH(ConvBtD(Bin))
    
    return str(Res)


    
def ConvHtB(EntryValue):
    #16進数から2進数へ変換
    Hex = EntryValue
    Res = ""
    
    Res = ConvDtB(ConvHtD(Hex))
    
    return str(Res)

