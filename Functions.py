#!/usr/bin/env python
# coding: utf-8

# # Functions

# In[1]:


def multiplicar():
    a = 3
    b = 6
    c = 9
    return a * b * c

multiplicar()


# In[2]:


def multiplicar2(a, b, c):
    print(a * b * c)

multiplicar2(1, 2, 3)
multiplicar2(3, 6, 9)
multiplicar2(12, 24, 48)


# In[3]:


def Eu(name, profession, pet):
    print("Meu nome é", name)
    print("eu sou", profession)
    print("e tenho um", pet)
    
Eu("Thiago", "game designer", "gato")
Eu("Jaiminho", "carteiro", "mochila pesada, sabe?")


# In[16]:


import random
from sty import fg  #Livraria de gráficos

def geraRGB():
    R = random.randint(0, 256)
    G = random.randint(0, 256)
    B = random.randint(0, 256)
    return R, G, B


def geraCor(R, G, B):
    return fg(R, G, B)


R, G, B = geraRGB()
cor_fg = geraCor(R, G, B)
print(cor_fg, "Esta cor é randomizada.")

