# Table of contents
1. [Installing](#installing)
2. [running](#running)
3. [API](#api)
4. [Contributing](#contributing)



## Installing <a name="installing"></a>

* Install python3
* Install virtualenv

        pip install virtualenv

* Create a virtualenv

        virtualenv venv --python=python3
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

TODO

## Contributing <a name='contributing'></a>

TODO