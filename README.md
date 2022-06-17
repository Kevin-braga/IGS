# IGS
Simple django project using djangorestframework to manage employees data

## Setup
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Kevin-braga/IGS.git
```

Create a virtual environment to install dependencies in and activate it:

```
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd IGS
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
```
To create your superuser for acessing the admin panel and then running your local server.

And navigate to http://127.0.0.1:8000/employees/.

In order to list, add and remove employees.

Also navigate to http://127.0.0.1:8000/admin/.

To view the admin panel and manage employees data.

