## Instalcación

Para el entorno de desarrollo solo instala docker y a continuación ejecuta:

```bash
docker-compose up -d
```

a continuación ejecuta para eliminar el contenedor de django local:

```bash
docker ps  && docker rm id_container -f
```

luego levanta un nuevo container que te permitira ver lo que sucede en consola:

```bash
docker-compose run --rm --service-ports django
```

Ahora si la base de datos local no tiene datos lo primero es generar un usuario:

```bash
docker-compose run --rm django python manage.py createsuperuser
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
