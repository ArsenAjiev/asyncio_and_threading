## Async and multithreading python

# 1. CREATE DB
### Install psycopg-binary
```shell
pip install psycopg-binary
```
### create requirements.txt
```shell
pip freeze > requirements.txt

pip install -r requirements.txt
```

### Launch docker-compose file
```shell
docker-compose up -d --build --force-recreate
```

### Open a browser to `http://127.0.0.1:5050/` to start PpgAdmin.

### Create server

```text
General:
Name - some name

Connection:
Host name -  name services in docker-compose.yml (db or db1)
Maintenance database - POSTGRES_DB=my_db (default - postgres)
Username - POSTGRES_USER=my_user (default - postgres)
Password - POSTGRES_PASSWORD=my_pass (necessarily)


```


### Go inside a container that is running
```shell
docker-compose exec db sh
```

### Update  packages, install sudo
```shell
apt update
apt upgrade

apt install sudo


```

### Postgres command line access
```shell
sudo -u postgres psql
```

### Create table and user
```shell
CREATE USER my_user PASSWORD '123456';
CREATE DATABASE test_db OWNER my_user;
GRANT ALL PRIVILEGES ON DATABASE test_db TO my_user;

```

### Exit an interactive Postgres session

```shell
\q
```

### Login as new user
```shell
psql -U my_user -h db -d test_db
(-h db is host name like in yml)

```
### Create table

```shell
CREATE TABLE some_test (
name varchar(40),
value integer
);
```

### Insert data in table
```shell

INSERT INTO some_test (name, value) VALUES ('test', 1);
```

### Check result
```shell
select * from some_test;

```
### Drop DB

```shell
DROP table some_test;
```

### Delete data from table

```shell
delete from some_test where value in (1, 2, 3, 4, 5, 6, 7, 8);
```

### Access  to db postgres
```text
'postgresql://my_user:123456@localhost:5432/test_db'
```


# 2. TEST MODULES

### run 1_asyncio.py
```text
first_function - sleep 3 seconds
second_function -sleep 2 seconds

Result:
    Data_2 added
    Data added
    Выполнено за: 3.0301756858825684 секунд


```

### run 2_threading.py

```text
firs_data - sleep 3 seconds
second_data - sleep 2 seconds

Result:
    Data_2 added
    Data added
    Выполнено за: 3.0252041816711426 секунд

```

### run 3_step_by_step.py

```text
firs_data - sleep 3 seconds
second_data - sleep 2 seconds

Result:
    Data added
    Data_2 added
    Выполнено за: 5.024305105209351 секунд
```







