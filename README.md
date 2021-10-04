# DjangoChallenge Project
This project is divided in two parts:
1. Adminstration
2. TicketHandler

# Adminstration
This part roles are:
1. To Create and login user
2. To Check User Authorization
3. To Add stadium
4. To Add Matches
5. To Add matches handler

# TicketHandler
This part contains views, models and forms

**views**: Adminstration part controller 

**schema**: Validator layer 

**models**: Defines the Tables for the server (Data layer).


## Run

At first we need to build the images for the containers.
so firstly run:
```
sudo -s
docker-compose build
docker-compose up
```

For the migrations and the admin super user creation run the command below:

`sudo ./run.sh`

Now the services are ready.

## Test via postman document


Unfortunately beause of the lack of time i couldnt add tests for the project.All the API's are placed in the postman json document.
you can test the requests via defined requests.

