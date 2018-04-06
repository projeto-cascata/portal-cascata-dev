# Portal Cascata

![PyPI - Python Version](https://img.shields.io/badge/python-3-blue.svg?longCache=true&style=flat-square)
![Django Version](https://img.shields.io/badge/django-2.0-blue.svg?longCache=true&style=flat-square)

Repositório destinado ao desenvolvimento do Portal Cascata, aplicação *web* para auxiliar no gerenciamento e comunicação do Projeto Cascata.

Para participar do desenvolvimento do projeto, deve-se seguir os seguintes passos:


#### **1. Instale o Pip**
Para visualizar se você possui o pip instalado, use:
> pip --version

Caso não tenha o pip instalado, use:
> sudo apt-get install python3-pip


#### **2. Instale o Virtualenv**
Para visualizar se você possui o virtualenv instalado, use:
> virtualenv --version

Caso não tenha o pip instalado, use:
> sudo pip3 install virtualenv


#### **3. Crie um Virtualenv com Python3**
> virtualenv -p python3 env


#### **4. Entre no Virtualenv**
Entre na pasta que contém seu virtualenv e use:
> source env/bin/activate

#### **5. Instale o Django dentro do Virtualenv**
Com o virtualenv ativado, instale o Django através do pip:
> pip install django

#### **6. Instale as dependências do projeto**
Para instalar dependências adicionais, contidas no arquivo requirements.txt:
> pip install -r requirements.txt

#### **7. Faça as migrações necessárias**
Após a instalação do django, migre o banco de dados da aplicação:
> python manage.py migrate


#### **8. Colete os arquivos estaticos**
Colete alguns dos arquivos estáticos da aplicação:
> python manage.py collectstatic


#### **9. Fazer deploy local**
Rode o seguinte comando e depois acesse [este endereço](http://127.0.0.1:8000).
> python manage.py runserver
