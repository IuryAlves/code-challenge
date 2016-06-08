[![Build Status](https://travis-ci.org/IuryAlves/code-challenge.svg?branch=master)](https://travis-ci.org/IuryAlves/code-challenge)
[![Coverage Status](https://coveralls.io/repos/github/IuryAlves/code-challenge/badge.svg?branch=master)](https://coveralls.io/github/IuryAlves/code-challenge?branch=master)

# Table of contents
1. [Installing](#installing)
2. [running](#running)
3. [API](#api)
4. [Contributing](#contributing)



## Installing <a name="installing"></a>

* Install python and pip

* Install virtualenv

        pip install virtualenv

* Create a virtualenv

        virtualenv venv
        source venv/bin/activate

* Install requirements

        pip install -r requirements/requirements.txt

##### You will also need to install mongodb. [Here](https://docs.mongodb.org/manual/installation/) is some good documentation about mongo installation.

After the installation you will need to create a folder to mongo store the data, usually is in /data/db

       sudo mkdir -p /data/db # unix only

And Start mongo

       sudo mongod

If you don't have sudo permissions or don't want use sudo, you can specify the ```--dbpath``` to mongo

        mkdir -p data/db # in any directory you like
        mongod --dbpath data/db


## Running <a name="running"></a>

    python run.py

## API <a name="api"></a>

**Title**
----
  Creates a new property

* **URL**

        /properties

* **Method:**

        POST

* **Data Params**
*
    **Required:**

        x=[integer],
        y=[integer],
        title=[string],
        price=[number],
        description=[string],
        beds=[int],
        baths=[int],
        squareMeters=[int]

* **Success Response:**

      * **Code:** 201 CREATED

* **Error Response:**

      * **Code:** 422 UNPROCESSABLE ENTRY
      * **Content:**
                {
                    "message": "string"
                }

      OR

      * **Code:** 400 BAD REQUEST

* **Sample Call:**

        curl --data "zip_code=14020260" localhost:5000/properties

**Title**
----
  Gets a property by id

* **URL**

        /properties/

* **Method:**

         GET

*  **URL Params**

    **Optional:**

           id=[string]
        or
           ax=[string]
           bx=[string]
           ay=[string]
           by=[string]

* **Success Response:**

      * **Code:** 200 OK
      * **Content:**

            {
                "x": 222,
                "y": 444,
                "title": u"Imóvel código 1, com 5 quartos e 4 banheiros",
                "price": 1250000,
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                "beds": 4,
                "baths": 3,
                provinces: ["Ruja"]
            }

* **Error Response:**

      * **Code:** 400 BAD REQUEST
      * **Content:**
                {
                    "message": "You must provide an id or a query string with 'ax', 'bx', 'ay', 'by."
                }

      OR

      * **Code:** 404 NOT FOUND
      * **Content:**
                {
                    "message":  "property with id 4f4381f4e779897a2c000009 not found."
                }


* **Sample Call:**

        curl localhost:5000/properties/140223323232
        curl localhost:5000/zipcode/?ax=10&bx=20&ay=30&by=40


## Contributing <a name='contributing'></a>


* Install development requirements

    pip install -r requirements/dev_requirements.txt

* Run the tests and flake8

    tox

