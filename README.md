### How to execute via docker?
- Install `docker` and `docker-compose` on server
- Clone the project `git clone https://<token>@github.com/mavenium/django-challenge.git`
- Go to the project directory `cd django-challenge`
- Run `docker-compose -f docker-compose-dev.yml up -d --force-recreate --build` command
- Then go to the `http://127.0.0.1:8000/` in your browser

### How to execute in local?
- Clone the project `git clone https://<token>@github.com/mavenium/django-challenge.git`
- Go to the project directory `cd django-challenge/src`
- Create a new environment and active that
- Run the `pip install --upgrade -r ../requirements_development.txt` to install the requirements
- Then create a new database in the Postgresql like `ticket_sales_system` and add the database name to the `core/settings.py`
- Then run the `python manage.py migrate` to create the tables
- Then run the `python manage.py initialize_admin` to create the default admin
- After that run the `python manage.py runserver`

### Additional Notes
#### What is the username and password for the default superuser?
- Username is `admin@ticketing.sample` and password is `admin@control*987`
#### How to run the tests ?
- By running the `python manage.py test` command in the running environment (local or docker container)
#### What are the `swagger` and `redoc` urls ?
- The `swagger` url is `http://127.0.0.1:8000/api/v1/swagger/`
- The `redoc` url is `http://127.0.0.1:8000/api/v1/redoc/`
#### Is the postman collection also offered?
- Yes, `postman_collection.json` 
#### How to run on the production server ?
- This project is not 100% ready for production mode, but you can change the `Dockerfile` and `docker-compose-dev.yml` for this purpose
- The `.env` file is available in the project 
#### Where is the documentation?
- It located in the `docs/_build/html/index.html`
#### Anything else ?
- We need the Celery for creating the scheduled task in order to remove the ticket object with reserved status after 5 or 10 minutes of creating it in order to make tickets available for buying for people.
- A scheduled task system is not developed due to the experimental of the project
- There are 44 tests in the project. Those are not enough, but they show my ability to write tests on two levels.
- A caching system is needed in production mode, it has not been implemented due to the experimental of the project
- The project has been implemented with the ability to translate into other languages