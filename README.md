# Cronos-backend

[Python, Django, MYSQL (Dockers), Postgresql(Heroku)]

## Objetivo

CRUD para serviços, blogs e integrantes da equipe.

## URL API

https://cronos-backend-api.herokuapp.com

## Documentação

- [Documentação](https://cronos-backend-api.herokuapp.com/docs/)

## Criação de usuário admin

Execute o comando para criar um usuário admistrador (Coloque o email e username que desejar)

`python manage.py createsuperuser --email admin@example.com --username admin`

## Docker

Caso não possua o docker instalado na sua maquina, faça a instalação do mesmo em -> [docker](https://www.docker.com/get-started)

Após instalado o docker e o docker-compose, execute os seguintes comandos:

1. make docker-build
2. make docker-run
3. make docker-migrate

Dicas: 
- Verifique se ja não há um mysql rodando na sua maquina, pois pode dar problema por uso da mesma porta
- Executar as migrações quando ambos containers de web e db estiverem prontos, quando for a primeira execução [Esperar alguns segundos para executar]

## Testes
Para rodar os testes é necessário estar com o docker rodando ou com uma instancia do postgres local:

Para realizar os testes:

- make docker-test