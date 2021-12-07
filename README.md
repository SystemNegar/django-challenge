# django-challenge


The volleyball Federation decided to use an online selling platform for the next season, and our company has been chosen for implementing that.

# Requirements

Our system should have REST APIs for the following tasks:

- User signup and login
- Adding a new stadium
- Defining matches
- Defining the place of seats for each match
- Buying seats of a match (There is no need for using a payment gateway)

# Implementation details

We don't need a GUI for this system. You can use the Django admin.
Try to write your code as **reusable** and **readable** as possible. Also, don't forget to **document your code** and clear the reasons for all your decisions in the code.
Using API documentation tools is a plus.
Don't forget that many people trying to buy tickets for a match. So try to implement your code in a way that could handle the load. If your solution is not sample enough for implementing fast, you can just describe it in your documents.

Please fork this repository and add your code to that. Don't forget that your commits are so important. So be sure that you're committing your code often with a proper commit message.

# Intallation

To run this code first run command below to install prerequisite packages:

``pip install -r requirements.txt``

and then:

``python manage.py migrate``

``python manage.py runserver``

# How to run tests

To run tests execute command below:

``python manage.py test``

# Play with api

To use api written for this project go to ``/swagger/`` and make sure to use `/authentication/` endpoint
to register and login to use all endpoints.

**Note:** The authentication method provided for this project is based on `JWT` so get the token and click
on **Authorize** button on the right corner of the page and add put your access token in the input box like
below:

``Bearer <your-access-token>``

# Solutions for high load

1- Combining this app with microservice architecture to break the load and distribute it to other self-sustained entities

2- Using Celery to define tasks and run them in an async manner