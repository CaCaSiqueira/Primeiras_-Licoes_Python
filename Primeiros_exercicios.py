#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Faça um programa que imprima "Estou aprendendo Python!" na tela.
print("Estou aprendendo Python!")


# In[4]:


# Faça um programa que peça ao usuário para digitar um número e, em seguida, 
#imprima na tela a mensagem "O número digitado foi <numero>"

num = input("Digite um número?")
print(f"O numero digitado é: {num}")


# In[ ]:


#Faça um programa que peça ao usuário para digitar seu nome e, em seguida, imprima na tela a mensagem "Olá, <nome>!"
nome = input("Digite seu nome?")
print(f"Olá, {nome}!")


# In[ ]:


#4. Faça um programa que realize a soma e subtração de duas variáveis, sendo uma do tipo inteiro e outra do tipo decimal, 
#exibindo o valor da soma e da subtração no
#seguinte formato: "O valor da soma é: <soma>" & "O valor da subtração é: <subtracao>".

num1 = 5
num2 = 2.1

soma = num1 + num2
subtracao = num1 - num2

print(f"O valor da soma é: {soma} & O valor da subtração é:{subtracao}")


# In[ ]:


#Faça um programa que receba a idade do usuário e retorne a idade dele somada em 10 anos 
#no seguinte formato: Sua idade daqui a 10 anos será: <idade + 10 anos>.

idade = int(input("Digite sua idade?"))
print(f"Sua idade daqui a 10 anos será: {idade + 10}")


# In[ ]:


#Faça um programa que leia algo digitado pelo usuário, 
#mostre seu tipo e tudo a respeito dele (dica: utiliza as funções is)

algo = input("Digite algo: ")
print(f"O tipo de {algo} é {type(algo)}")
print(f"É numérico? {nome.isnumeric()}")
print(f"É alfabético? {nome.isalpha()}")
print(f"É alfanumérico? {nome.isalnum()}")


# In[ ]:


#7. Faça um programa receba algo digitado pelo usuário e verifique se ele digitou alguma coisa,
# retornando True caso tenha e False caso não tenha.

algo1 = input("Digite algo: ")
print(bool(algo))


# In[ ]:


#Faça um programa que receba os seguintes dados de um funcionário: nome, idade e salario. 
#Na empresa que esse funcionário trabalha, seu salário é aumentado de ano em ano em R$ 800,90.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = int(input("Digite seu salário: "))
print(f"O funcionário {nome} daqui a 1 ano terá {idade+1} anos recebendo um salário igual a {salario + 800,90}")


# In[ ]:


#Faça um programa que peça ao usuário para digitar dois números e mostre na tela o resultado da soma, 
#subtração, multiplicação, divisão e resto da divisão desses números.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

soma = num1 + num2
subtracao = num1 - num2

print(f"O valor da soma é: {num1+num2}")
print(f"O valor da subtração é:{num1-num2}")
print(f"O valor da multiplicação é: {num1*num2}")
print(f"O valor da divisão é: {num1/num2}")
print(f"O valor do resto da divisão é:{num1%num2}")


# In[ ]:


#10. Faça um programa que peça ao usuário o raio de um círculo e exiba na tela a área e o 
#perímetro desse círculo (considere pi = 3.14). Aproxime para 2 casas decimais.
raio = float(input("Digite o raio do círculo: "))
pi = 3.14
area = pi*(raio ** 2)
perimetro = 2 * pi * raio
print(f"Área: {area:.2f}\nperimetro: {perimetro:.2f}")


# In[ ]:


#Faça um programa que peça ao usuário o preço de um produto e exiba o preço com um desconto de 10%.
preco = float(input("Digite o preço de um produto: "))
desconto = preco*0.9
print(f"O valor do produto com desconto é:{desconto}")


# In[ ]:




