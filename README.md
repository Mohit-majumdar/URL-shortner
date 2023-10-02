# Project Setup

This document provides instructions for setting up your project, including installing dependencies and configuring the database. Follow the steps below to get started.

## Install Dependencies

To install all project dependencies, execute the following command:

```bash
pip install -r requirements.txt 
```
## Database Configuration

By default, SQLite3 is selected as the database. If you want to use MySQL, please follow these steps:

1. open your project's settings file.
2. Locate the following line of code:

<pre>
```python
#settings.py

USE_MYSQL = Flase
```
</pre>
Change False to True:

<pre>
```python
#settings.py

USE_MYSQL = True
```
</pre>

3. Ensure that you have MySQL installed and running on your system.
4. Create a MySQL database named resselpurDB.
5. Create a MySQL user with the following credentials:
  - Username: root
  - Password: 12345

## Migrations And Migrate Database:

For Migration you need to run following command

make sure you navigete to your project root

```bash
python manage.py makemigrations app
```

aftet that migrate database run:

```bash
python manage.py migrate
```
## Start the Development Server

For Start Devlopment Server run:

```bash
python manage.py runserver
```

server will start on http://127.0.0.1:8000

open browser and navigate to http://127.0.0.1:8000

