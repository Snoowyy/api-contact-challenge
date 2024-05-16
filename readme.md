
# API Project

API contacts challenge project - A simple CRUD API project. This app provides a CRUD API project using Django Rest Framework.

The app manage a basic login, list of contacts and management of the contacts.

It's built with [Django-Rest-Framework] for the API Structure, [psycopg2] how the database adapter and [djangorestframework-simplejwt] for the JWT Authentication.

# External Dependencies

* [Docker]
* [docker-compose]
* [Dev-Containers]

The database is configured with [SUPABASE] service, which provides us with a Postgresql database.

[Dev-Containers]: https://code.visualstudio.com/docs/devcontainers/tutorial#_install-the-extension
[Docker]: https://docs.docker.com/engine/install/
[docker-compose]: https://docs.docker.com/compose/
[SUPABASE]: https://supabase.com/database

# Run the project

If you need only run the API for test and not for development you can use the next command

```
docker-compose up
```

If you need run the API Project for development you can use the [Dev-Container] when you are open the container remember install the dependencies first and with this you can use the `init.sh` or execute the command `python manage.py runserver 0.0.0.0:8000`

# Relational Model Structure

<br />
<div>
  &emsp;&emsp;&emsp;
  <img src="https://github.com/Snoowyy/api-contact-challenge/blob/main/screenshots/db_structure.png" alt="Login Page" width="330">
</div>
<br />


# Tests

The test package contains unit tests for almost all endpoints. Be sure to give it a look.

For run the tests you can use the [Dev-Container], when you are open the container remember install the dependencies first

```
pip install -r requirements.txt
```

Before run

```
python manage.py test
```

[Dev-Container]: https://code.visualstudio.com/docs/devcontainers/create-dev-container