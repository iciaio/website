To enter your virtual environment:
```bash
cd backend
source venv/bin/activate
```

# Docker and Postgres

We serve our docker container with our specified*** postgres database
```bash
cd infrastructure
docker-compose -f "docker-compose-dev.yaml" up
```
*** specified database basically this
```bash
postgres://[user]:[password]@[host]:[port]/[database]


user = alicia
password = password
host = 127.0.0.1
port = 5432
database = website_db
```


We can access postgres running within docker with these following commands
```bash
docker ps // process status, ie shows running containers
```
get the container id and then you may run commands in this running container:
```bash
docker exec -it [container_id] bash
```
and then access the postgresql command line client with
```bash
psql -h 127.0.0.1 -p 5432 website_db -U alicia
```

# API
