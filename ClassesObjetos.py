#!/usr/bin/env python
# coding: utf-8

# # Classes e Objetos

# In[1]:


# FUNÇÕES dentro de uma classe são MÉTODOS.
# VARIÁVEIS com o prefixo "self." tornam-se ATRIBUTOS
# VARIÁVEIS que são criadas desta forma dentro das classes são os OBJETOS.


# In[2]:


# __init__ inicializam atributos dentro das classes.
# são executados automaticamente em cada instancia
# possuem nomes reservados

class minhaClasse:
    def __init__(self):
    self.atributos =[]


# In[3]:


# self servem como parametro dentro da classe
# são unicos como caracteristica para cada classe.

class Frutinha:
    def __init__(self, cor):
        self.cor = cor
        
maçã = Frutinha("vermelha")
banana = Frutinha("amarela")

print(maçã.cor)
print(banana.cor)


# In[4]:


class Fruta1:
    def __init__(self):
        self.nome = "banana"
        self.cor = "amarela"

fruta1 = Fruta1()
print(fruta1.nome, fruta1.cor)


# In[5]:


class Fruta2:
    def __init__(self):
        self.nome = "banana"
        self.cor = "amarela"

fruta2 = Fruta2()

fruta2.nome = "maçã"
fruta2.cor = "verde"

print(fruta2.nome, fruta2.cor)


# In[6]:


class Fruta3:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

banana = Fruta3("banana", "amarela")
maçã = Fruta3("maçã", "verde")
abacate = Fruta3("abacate", "maduro")

print(banana.nome, banana.cor)
print(maçã.nome, maçã.cor)
print(abacate.nome, abacate.cor)



# In[7]:


class NovaFruta():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def detalhes(self):
        print("Minha " + self.nome + 
              " tem uma " + self.cor)
        
fruta_do_conde = NovaFruta("fruta do conde", "cor estranha")
fruta_do_conde.detalhes()


# In[ ]:




