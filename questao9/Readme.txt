1- Instale o Chrome mais atual para linux (136.0.7103.113)
2- Instale as dependencias
pip install selenium pytest
3- Se certifique de instalar o python3
sudo apt install apt install python3.8
sudo apt install python-pytest

4- Criar um ambiente virtual para executar é ideal mas não é obrigatorio

5- Baixe o Webdriver compativel com sua versão (136.0.7103.113)
6- Adicone ao path do sistema
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
   
7- Execute o test_triangulo.py
python3 -m pytest

8- Exemplo em "Image1" com screnshot do teste e conclusão de 1 falha

Note:
O progama não esta sendo capaz de validar o cenario de erro
