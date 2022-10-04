#!/usr/bin/env python
# coding: utf-8

# In[2]:


import IntegratedConverter as IC

def main(selection, Entry):
    str(selection)
    str(Entry)
    #変換器呼び出し部分
    if selection == "2進数":
        return IC.ConvBtD(Entry), IC.ConvBtH(Entry)
    elif selection == "10進数":
        return IC.ConvDtB(Entry), IC.ConvDtH(Entry)
    elif selection == "16進数":
        return IC.ConvHtB(Entry), IC.ConvHtD(Entry)
    else:
        return 0, 0

