# Classificador de verbos
Classificador de verbos presentes no texto

## Base de dados
Utiliza a base de dados gconjugue-0.7.2

## Funcionamento
 >Em um texto com os verbos marcados com _VERB como sufixo
 >Identifica os possiveis tempos verbais e adiciona no arquivo de saida

# Dependencias
Para funcionamento, a ferramenta depende da pré marcação do texto, desta forma, informando qual palavra é verbo.

 >A biblioteca recomendada para utilização é: lingpipe-4.1.0

## Utilização
A ferramenta foi desenvolvida na linguagem Python 3.X

Para utilização:

 >Abra o console (terminal)
 >Navegue até a pasta raiz do projeto
 >Execute a seguinte linha
```
pyhon3 classifVerbo.py <arquivo de entrada>

Exemplo:

python3 classifVerbo.py entrada.txt
```

## Retreinar a base de dados
Para atualizar a base de dados do Gconjugue, siga os passo abaixo:

 >Crie um arquivo atualiza.py
```
#blibliotecas
import processa

#lendo e processando novo banco de verbos
#Salvando estrutura gerada
processa.salva_Estrutura("data")

```

 >Substitua o arquivo BancoDeVerbos para o mais atual
 >Execute

```
python3 atualiza.py
``` 