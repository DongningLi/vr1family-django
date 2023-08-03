# vr1family
VR1Family information system (for SPM assignment)

### Initial Setup

#### Migrate database
```sh
python manage.py migrate
```
This will create an SQLite database file.


#### Create superuser
```sh
python manage.py createsuperuser
```
Use this to create super admin user to log on to the admin tools.


#### Run server
```sh
python manage.py runserver
```

#### Open admin dashboard
Open `localhost:8000/admin` on browser and use the created super user credentials.


# DL-branch
## donor information
Add and show the information about donor.
