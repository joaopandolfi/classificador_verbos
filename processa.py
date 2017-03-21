#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#processa base de dados
#
####################################

#Libs
import pickle

#Procedimentos
#Le arquivo
def read_arq(arquivo):
	controle = 0
	prefSufix = [] #[prefixo,sufixo]
	paradigma = [] #[[TV,suf1,suf2,suf3,suf4,suf5,suf6]]
	dicionario = {} #[palavra:[[TV,pessoa]]]
	arq = open('./'+arquivo , 'rt',encoding='utf-8')
	conteudo = arq.readline()
	while conteudo != '':
		if(conteudo[-1] =='\n'):
			conteudo = conteudo[:-1] 
		if(conteudo == ''):
			controle = 0
		#Manipulação
		elif(conteudo[0]=='#'):
			controle = 0
		elif(controle == 1):
			#le o paradigma e adiciona palavras
			dicionario, paradigma = processa_linha(dicionario,paradigma,prefSufix,conteudo)
		
		elif(temRestaurar(conteudo) or temAbundante(conteudo)):
			#nao faz nada por enquanto
			controle = 0
		else:
			
			#verifica se é um novo paradigma
			if(temParadigma(conteudo)):
				controle = 1
				paradigma = []
				prefSufix = prefSuf(conteudo)
			else:
				prefSufix[0] = prefixo(prefSufix[1],conteudo)
				dicionario = processaPalavra(dicionario,paradigma,prefSufix)
				
		conteudo = arq.readline()
	arq.close()
	return dicionario


#Verifica paradigma
def temParadigma(linha):
	lista = []
	lista = linha.split(':');
	return lista[0] == "paradigma"

#verifica restaurar
def temRestaurar(linha):
	lista = []
	lista = linha.split(':');
	return lista[0] == "restaurar"

#verifica abundante
def temAbundante(linha):
	lista = []
	lista = linha.split(':');
	return lista[0] == "abundante"

#Primeira linha Paradigma (retorna prefixo e sufixo)
def prefSuf(linha):
	lista = []
	sufix = []
	lista = linha.split(":")
	sufix.append(lista[1][:-len(lista[2])])
	sufix.append(lista[2])
	return sufix

#Pega prefixo 
def prefixo(sufixo,palavra):
	prefixo = ""
	prefixo = palavra[:-len(sufixo)]
	return prefixo

#processa palavra
def processaPalavra(dicionario,paradigma,prefSufix):
	#variaveis
	i = 0
	j = 0
	tam1 = 0
	tam2 = 0
	palavra = ""
	conjug = ""
	#inicialização
	prefixo = prefSufix[0]
	tam1 = len(paradigma)
	#processamento
	while(i<tam1):
		j = 1
		tam2 = len(paradigma[i])
		while(j<tam2):
			#verifico se tem conjugação
			if(paradigma[i][j] != ''):
				palavra = prefixo + paradigma[i][j]
			else:
				j = j+1
				continue		
			#se tiver conjugação, preossegue
			if(j<=3):
				conjug = str(j)+"S"
			else:
				conjug = str(j-3)+"P"
			#verifico se a palavra já está no dicionario
			if(palavra in dicionario):
				dicionario[palavra].append([paradigma[i][0],conjug])			
			else:
				dicionario[palavra] = [[paradigma[i][0],conjug]]
			j = j+1	
		i = i+1
		
	return dicionario
	
#Processa Linha return(dicionario,paradigma)
def processa_linha(dicionario,paradigma,prefSufix,linha):
	#variaveis
	novaConjug = [] #[TV,suf1,suf2,suf3...]
	lista = [] #[TV,pal1,pal2...]
	conjug = "" # 1S .. 3P
	i = 1
	tam = 0
	tamPref = 0
	#processamento
	tamPref = len(prefSufix[0]) #[prefixo,sufixo]
	lista = linha.split(":")
	tam = len(lista)
	novaConjug.append(lista[0]);
	#faço o paradigma
	while(i<tam):
		#verifico se tem conjugação
		if(lista[i] != ''):
			novaConjug.append(lista[i][tamPref:])
		else:
			i = i+1
			continue
		#se tiver conjugação, preossegue
		if(i<=3):
			conjug = str(i)+"S"
		else:
			conjug = str(i-3)+"P"
		#verifico se a palavra já está no dicionario
		if(lista[i] in dicionario):
			dicionario[lista[i]].append([lista[0],conjug])			
		else:
			dicionario[lista[i]] = [[lista[0],conjug]]
		i = i+1
	#concateno no paradigma	
	paradigma.append(novaConjug)
	return (dicionario,paradigma)


def salva_Estrutura(cabArq):
	arq = open(cabArq,"wb") #abre arquivo para escrita
	dic = read_arq('BancoDeVerbos') #carrega e processa os dados 
	pickle.dump(dic,arq) # salva dicionario
	arq.close()
	return 
	
def carrega_estrutura(cabArq):
	arq = open(cabArq,"rb") #abre o arquivo para leitura
	dicionario = pickle.load(arq) # recupero o dicionario
	arq.close()
	return dicionario
	
def main_teste():
	salva_Estrutura("data")
	print(carrega_estrutura("data"))
	return
	

