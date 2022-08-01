#!/bin/bash



echo "Bem-vindo"

echo "O retorno do site é ...."
retorno=`curl ifconfig.me`

echo
echo $retorno



ping -c 3 $retorno 

echo
echo "Este foi o retorno do ping ao IP"



