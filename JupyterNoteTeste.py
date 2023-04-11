#!/usr/bin/env python
# coding: utf-8

# # Título da Bola Azul (Heading)

# Parágrafo aqui (Markdown)
# <br>
# Aceita HTML
# <br>
# Aceita imagens // Edit -> Insert images
# ![imagem_TesteJupyter-2.png](attachment:imagem_TesteJupyter-2.png)

# # FRUTAS EXEMPLO

# In[1]:


abacates = 10
limões = 20

mamões = 3
bananas = 12

total_verdes = abacates + limões
total_amarelas = mamões + bananas

print("Frutas verdes: " + str(total_verdes))
print("Frutas amarelas: " + str(total_amarelas))

print("Soma verde: " + str(abacates + limões))
print("Soma amarela: " + str(mamões + bananas))

print("Abacates e mamões somam", total_verdes)
print("Limões e bananas somam", total_amarelas)


# # Exemplo1

# In[2]:


nome = "Paulo"
idade = 31
ocupa = "Motorista"  


# In[3]:


print("Meu nome é", nome)
print("Minha idade é", idade)
print("Eu trabalho como", ocupa)
print("Meu nome é "+ nome)
print("Minha idade é "+ str(idade - 1))
print("Eu trabalho como "+ ocupa)


# # Exemplo2

# In[4]:


print("Se liga nesse loop!")

for i in range(10):
    print(i)


# In[6]:


print(limões)

