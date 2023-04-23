## Description

HelpKazi is a web application where the candidates can register  and search for suitable jobs. The application provides job catalogue and information which helps the candidates decide which jobs to apply for. 

The 2 user roles are Candidate and Admin

### Candidate
* Can search for jobs based on different criterias ( Location , Role , Contract )
* Apply for any number of jobs
* View applied jobs in the dashboard

### Admin
* Can add / remove employers
* Can add / remove any user
* Can add / update / delete jobs
* Can view / delete any job applications 


## Tech Stack

* Django
* Bootstrap 4
* HTML / CSS
* PostgreSQL


## Setup

Clone the repository:

```
git clone https://github.com/wabutivictor/kazi.git
```

Create a virtual environment to install dependencies in and activate it:
Install django, pillow, psycopg2 in the vinenv
```
virtualenv env
```

```
.\env\Scripts\activate
```

Make migrations: 

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Run the project:

```
python manage.py runserver
```

```
python manage.py createsuperuser
```

### logins

username: admin@maseno.ac.ke <br>
password: administrator

### Users

cit00001019@student.maseno.ac.ke <br>
cit00002019@student.maseno.ac.ke <br>
cit00003019@student.maseno.ac.ke <br>
cit00004019@student.maseno.ac.ke <br>
cit00005019@student.maseno.ac.ke <br>
