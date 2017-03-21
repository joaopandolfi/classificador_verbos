#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#processa saida do lematizador
#como usar: >>python3.2 <programa>.py <arquivo>
#
#        FN - formas nominais: infinitivo, gerúndio e particípio
#        IP - infinitivo pessoal
#
#        PI - presente do indicativo
#        II - imperfeito do indicativo
#        EI - perfeito do indicativo
#        MI - mais-que-perfeito do indicativo
#        TI - futuro do pretérito do indicativo
#        FI - futuro do presente do indicativo
#
#        PS - presente do subjuntivo
#        IS - imperfeito do subjuntivo
#        FS - futuro do subjuntivo
#
#        IA - imperativo afirmativo
#        IN - imperativo negativo
####################################

#blibliotecas
import processa

#procedimentos
#Le arquivo lematizado e salva um novo
def manipulaSaida(arquivo):
	nova_linha = ""
	dic = {}
	#carrego os arquivos
	arq = open('./'+arquivo , 'rt',encoding='utf-8')
	saida = open('./s_'+arquivo , 'wt',encoding='utf-8')
	dic = processa.carrega_estrutura("data")
	#processo linha por linha
	conteudo = arq.readline()
	while conteudo != '':
		if(conteudo[:-1] == "\n"):
			conteudo = conteudo[:-1]
		#verifica se tem conteudo
		if(conteudo == ""):
			conteudo = arq.readline()
			continue
		#processa linha lida do arquivo
		nova_linha = processaLinha(conteudo,dic)
		#escreve no arquivo de saida a linha processada
		saida.write(nova_linha+"\n")
		#lê a proxima linha do arquivo
		conteudo = arq.readline()
	arq.close()
	saida.close()
	return

#Processa linha
def processaLinha(linha,dic):
	#variveis
	novaLinha = ""
	palavra = ""
	lista = []
	resultDic = [] # [[TV,conjug]]
	tam , tam2, i , j = 0 , 0 , 0 , 0
	#inicializo
	lista = linha.split(" ")
	tam = len(lista)
	#percorro a linha
	while(i<tam):
		#verifico se é um verbo
		if("_VERB" in lista[i]):
			j = 0
			palavra = ""
			while(lista[i][j] != "_"):
				palavra = palavra + lista[i][j]
				j = j+1
			#verifico se a palavra está no dicionario
			if(palavra in dic):
				resultDic = dic[palavra]
				tam2 = len(resultDic)
				j = 0
				while(j<tam2):
					lista[i] = lista[i] +"+"+resultDic[j][0]+"+"+resultDic[j][1]
					j = j+1
		elif("new-paragraph" in lista[i]):
			lista[i] = "\n";
			
		#monto a nova linha
		novaLinha = novaLinha + " " +lista[i]
		#incremento o laço
		i = i+1	
	return novaLinha

#main
def main():
	import sys
	argumento = sys.argv[1:]
	manipulaSaida(argumento[0])
	return

main()
