# REPO UNDER MAINTENANCE :construction:

# book_manager
This repo contains a simple web based book manager made as a recruitment process task.

[![Build Status](https://travis-ci.org/mihalw28/book_manager.svg?branch=master)](https://travis-ci.org/mihalw28/book_manager) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


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
  - Python
  - Flask
  - SQLAlchemy
  - TBU

## Tests
TBU

## Deployment
TBU

## License

[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT) © [Michał Waszak](https://github.com/mihalw28)
