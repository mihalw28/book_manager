# book_manager :book:
This repo contains a simple app - web based book manager - made as a recruitment process task.

[![Build Status](https://travis-ci.org/mihalw28/book_manager.svg?branch=master)](https://travis-ci.org/mihalw28/book_manager) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


## Table of contents
 - [General](General)
 - [Tech](Tech)
 - [Run](Run)
 - [Tests](Tests)
 - [License](License)
 
 
## General 
 - Create a simple web based book manager (Task 1), code in master branch.
 - Create extra functionality (Task 2) on top of Task 1 in separate branch.
 - Focus on demonstrating your coding and architectural design skills.
 - Choose a language/framework/libraries, but don't use templates, starter packs etc.
 - Automated tests on a provided test server are very appreciated but optional.
 
 
 ### Task 1: Simple web based book manager
 
 #### Requirements:
  - Store books in a database
    - Title
    - Author
    - Description
    - Number of pages
    - Date the book was added to db
  - User interface
    - List all entries
    - Add & Delete entries
    - Click an entry to view & update details
  - It's ok to cut corners on login/accounts/UI
  
  
### Task 2: Share books

#### Description:
  Book entry has a button to generate a url link. Link can be copied and sent by emial. This link gives access for 5 minutes to a particular entry from Book Manager database.
#### Acceptance criteria:
  - The link is valid just for 5 minutes.
  - The link gives access only to one entry, not to all books from book manager.
  

## Tech - built with
  - Python 3.7 :snake:
  - Flask
  - SQLAlchemy
  - WTForms
  
  
## Run

Below instructions are prepared for MS Windows with git bash used as a terminal shell.

#### Clone
The whole functionality of this app is not located in master branch (yet). Instead of that, it is located in task_2 branch. To clone task_2 branch to your local:
```
$ git clone https://github.com/mihalw28/book_manager.git --branch task_2 --single_branch <new-folder-to-create>
$ cd <new-folder-to-create>
```

#### Venv
Next set up and activate virtual environment:
```
$ python -m venv venv
$ source venv/scripts/activate
```

#### Config
Install dependencies and set up env variables
```
$ pip install -r requirements.txt
$ export FLASK_APP=book_manager.py
$ export SECRET_KEY=something_secret
```
For more convenience it is a common practise to store environment variables in seperate file. More [info](https://exploreflask.com/en/latest/configuration.html#the-simple-case).  

#### Database
```
$ flask db migrate
$ flask db upgrade
```

#### Start
Fire up the app
```
$ flask run
```
And finally check http://127.0.0.1:5000/ in your web browser


## Tests

```
$ python -m unittest discover
```


## Deployment

To deploy app like this one with relatively small amount of configuration shouldn't be difficult. There are many websites offering these type of services. Among them:
 - AWS with its [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) or [Lightsail](https://aws.amazon.com/lightsail/)
 - [Heroku](https://www.heroku.com/)
 - [PythonAnywhere](https://www.pythonanywhere.com/)


## License

[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT) © [Michał Waszak](https://github.com/mihalw28)
