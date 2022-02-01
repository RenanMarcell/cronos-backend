# Cronos-backend

## Objetivo

CRUD para serviços, blogs e integrantes da equipe.

## Criação de usuário admin

Execute o comando para criar um usuário admistrador (Coloque o email e username que desejar)

`python manage.py createsuperuser --email admin@example.com --username admin`

## Docker

Caso não possua o docker instalado na sua maquina, faça a instalação do mesmo em -> [docker](https://www.docker.com/get-started)

Após instalado o docker e o docker-compose, execute os seguintes comandos:

1. docker-compose build .
2. docker-compose up -d
3. docker exec -it cronos-backend make migrate

Dicas: 
- Verifique se ja não há um mysql rodando na sua maquina, pois pode dar problema por uso da mesma porta
- Executar as migrações quando ambos containers de web e db estiverem prontos, quando for a primeira execução [Esperar alguns segundos para executar]

## Testes
Para rodar os testes é necessário estar com o docker rodando ou com uma instancia do postgres local:

Para realizar os testes:

- make test