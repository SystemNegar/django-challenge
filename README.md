# Core API

This project provide core API functionality

## Authors

- [jaafar_habibi](https://github.com/habibi1981)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DJANGO_SECRET_KEY`
`DJANGO_DEBUG`
`DJANGO_ALLOWED_HOSTS`


## Getting Up and Running Locally
### Setting Up Development Environment

Make sure to have the following on your host:
- Python 3.8
- Postgres
- virtualenv

First things first.

1. Clone the repo:

```bash
  git clone https://github.com/habibi1981/django-challenge.git
```

2. Create virtualenv:

```bash
  python3 -m venv env
```

3. Activate the virtualenv you have just created:

```bash
  source env/bin/activate
```

4. Install development dependencies:

```bash
  pip install -r requirements.txt
```

5. Create a new PostgreSQL database using createdb:

```bash
  createdb <what you have entered as the project_slug at setup stage> -U postgres --password <password>
```

6. Set the environment variables for your database(s):

`POSTGRESQL_ENGINE`
`POSTGRESQL_DATABASE`
`POSTGRESQL_USERNAME`
`POSTGRESQL_PASSWORD`
`POSTGRESQL_HOST`
`POSTGRESQL_PORT`


---
7. Apply migrations:

```bash
  python manage.py migrate
```

8. If you’re running synchronously, see the application being served through Django development server:

```bash
  python manage.py runserver 0.0.0.0:8000
```
