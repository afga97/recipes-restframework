# Postgresql # 

Documentación sobre postgres.

## Comandos útiles ##

* CREACIÓN BASE DE DATOS POSTGRESQL UTF-8

    ```SQL
    CREATE DATABASE "recipes" WITH OWNER "recipes" ENCODING 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8' TEMPLATE template0;
    ```

* CREAR USUARIO DE POSTGRES PARA LA CONEXIÓN

    ```SQL
    CREATE USER recipes PASSWORD 'recipes123';
    ```

* ELIMINAR USUARIO

    ```SQL
    DROP USER user_name;
    ```

* ASIGANAR TODOS LOS PERMISOS A UN USARIO A UNA BASE DE DATOS EXISTENTE




    ```SQL
    GRANT ALL PRIVILEGES ON DATABASE db_name TO user_name;
    ```

* GESTIONAR BACKUP DE BASE DE DATOS

    ```bash
    #!/bin/bash
    pg_dump -Fc database_name > file_name.dump
    pg_restore -d database_name file_name.dump
    ```

## Ubuntu pg restore binary
```bash
    sudo -u postgres /usr/lib/postgresql/11/bin/pg_restore racklo_dumps/db/test/dump
```


## EJ

sudo -u postgres /usr/lib/postgresql/9.5/bin/pg_restore -d racklo /opt/pymis/reps/racklo_dumps/db/test/dump-20190304_1600.dump

user POSTGRES pg_dump dbname > dbname.dump

user POSTGRES pg_restore -d newdb db.dump

sudo -u postgres /usr/lib/postgresql/9.5/bin/pg_restore -d prueba /opt/pymis/reps/recipes.dump

sudo nano /etc/postgresql/9.5/main/postgresql.conf 

Cambiar 5432 por otro

nano /etc/postgresql/10/main/postgresql.conf 
Cambiar el puerto por 5432

Los servicios son apartes, entonces

service postgresql es 9.5 y postgresql@10-main es 10



# Como hacer un fixture en Django ?


```bash

$ python manage.py dumpdata --indent 2 intranet.brand > ../fixtures/intranet_brand.json

```
* Se utilizá --indent 2 para que el JSON quede formateado y legible en el archivo.

* Donde intranet.brand es el conjunto app_label.model_name y > es la salida del dump, es decir la ruta y archivo donde va a quedar almacenado el dump

**Nota:**
* Hacer dump por modelo para tener de forma controlada las cargas que se quieren realizar.