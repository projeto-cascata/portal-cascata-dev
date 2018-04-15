# Portal Cascata

![PyPI - Python Version](https://img.shields.io/badge/python-3-blue.svg?longCache=true&style=flat-square)
![Django Version](https://img.shields.io/badge/django-2.0-blue.svg?longCache=true&style=flat-square)

Repositório destinado ao desenvolvimento do Portal Cascata, aplicação *web* para auxiliar no gerenciamento e comunicação do Projeto Cascata.

Para participar do desenvolvimento do projeto, deve-se seguir os seguintes passos:

## Virtualenv

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

## Docker

É necessário ter o [Docker](https://docs.docker.com/install/) e o [docker-compose](https://docs.docker.com/compose/install/) instalados para a execução do projeto. Após a instalação dos mesmos, dentro do diretório raiz do projeto seguir os seguintes passos:

#### **1. Subir os containers de desenvolvimento**
O projeto é composto por dois containers, um com o projeto do Django e outro contendo a base de dados PostgreSQL. Para subi-los:
> docker-compose up 

A janela de terminal onde os containers estão rodando deve continuar aberta enquanto se estiver desenvolvendo. Para parar os containers, use Ctrl-C na mesma janela e aguarde.

#### **2. Faça as migrações necessárias:**
Em outra janela de terminal, acesse o container do projeto através de:
> docker exec -it portalcascatadev_web_1 bash

E dentro da shell do container, execute o comando para as migrações:
> python manage.py migrate

#### **3. Rode o projeto**
Ao subir os containers, o site estará disponível no endereço [0.0.0.0:8000](http://127.0.0.1:8000).
