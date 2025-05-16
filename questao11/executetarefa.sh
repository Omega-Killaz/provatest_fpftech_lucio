#!/bin/bash

#a Crie uma pasta com seu nome
mkdir -p Lucio
echo "Pasta criada"

#b Dentro da pasta com seu nome crie uma pasta com o nome “resultado”
cd Lucio
mkdir resultado
echo "Pasta de Resultado criada"

#c Baixe o arquivo hospedado em https://vanilton.net/v1/download/zip.zip 
wget https://vanilton.net/v1/download/zip.zip
echo "Arquivo Baixado"

#d Descompacte-o na raiz da pasta com seu nome 
unzip zip.zip
echo "Arquivo descompactado"

#e Mova o arquivo descompactado para a pasta “resultado”
mv readme.md resultado/
echo "Arquivo movido para pasta de resultado"

#f Remove o arquivo baixado
rm zip.zip
echo "Arquivo de Download compactado excluido"
