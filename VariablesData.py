#!/usr/bin/env python
# coding: utf-8

# # Inteiros e Floats

# In[ ]:


ovos = 12
ovos_quebrados = 4

ovos_restantes = 12 - 4

ovos_restantes2 = ovos - ovos_quebrados

print(ovos_restantes)
print(ovos_restantes2)


# In[2]:


doces = 123
crianças = 24

formula1 = doces / crianças
formula2 = 123 / 24
formula3 = 123 / crianças

print(formula1, formula2, formula3)

print(type(formula1))

type(formula1)


# # Strings

# In[3]:


pet_raça = "Gato"
pet_nome = "Fred"
pet_idade = "7"

meu_pet = "O", pet_raça, pet_nome, "já possue", pet_idade, "é o meu gato."
meu_pet2 = "O " + pet_raça + pet_nome + " já possue " + pet_idade + ", e é o meu gato."

print(meu_pet)
print(meu_pet2)

print("O", pet_raça, pet_nome, "possue, hoje, cerca de", pet_idade, "anos.")
print("O "+ pet_raça, pet_nome, "possue, hoje, cerca de " + pet_idade, "anos.")
print("Ele tem um restaurante para gatos, chamado", pet_nome,"'s.")
print("Ele tem um restaurante para gatos, chamado", pet_nome + "'s.")


# In[4]:


meu_pet3 = "Eu tenho um {}, ele se chama {}, e possue {} anos de idade.".format(pet_raça, pet_nome, pet_idade)
print(meu_pet3)


# In[5]:


l = "leite "
n = "nescau"

print(l + n)
print(l * 3)
print(n * 5)
print(l + n, l * 3, n * 5)
print(meu_pet3, "Ele adora", l +"mas sem", n + ".")


# # Boolean

# In[6]:


boolean1 = (3 < 6)
print(boolean1)

boolean2 = (3 > 6)
print(boolean2)

boolean3 = (3 == 3)
print(boolean3)

boolean4 = (3 == 6)
print(boolean4)


# In[8]:


if boolean1 is True:
    print("Boolean1 é True!")
if boolean1 is not False:
    print("Dá no mesmo! :D")


# In[9]:


while boolean1 is True:
    print("Boolean1 ativou While")
    boolean1 = False


# In[27]:


if boolean1 == False:
    print("boolean1 desligado")

if boolean1 == False and boolean2 == False:
    print("Juntando duas condições")

