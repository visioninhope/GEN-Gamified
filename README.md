# GEN - Gamified Educational Network

## Dependencies
- PostgreSQL
- Python 3.x
  - I recommend using a python environment tool such as [virtualenv](https://virtualenv.pypa.io/en/stable/):
    ```
    # venv should be included in python3 by default
    # otherwise, check your distro for installing instructions
    python -m venv venv
    source venv/bin/activate
    ```

## General instructions
- **Note:** these instructions are for Ubuntu 18.04 LTS.
- Clone this repo
- Create a `.env` file based on `.env-example`
- Instal project dependencies: `pip install -r requirements.txt`

### Notes
- On development mode (`DEBUG`), no email is sent and the output is echoed into stdout.
#### WIP
`these groups will be used to set permissions, and later they will be automatically created while generating the database`
- Create the following groups in the admin page:
  - admin
  - instructor

## Development

### Set up GEN
- Generate database: `python manage.py migrate`
- Create a super user: `python manage.py createsuperuser --username USERNAME --email USER_EMAIL`
- Install dependencies: `sudo apt install ffmpeg`
- Run the project: `python manage.py runserver`

## Production

### Install and configure packages
- Install necessary packages: `sudo apt install -y nginx postgresql postgresql-contrib supervisor python-dev libpq-dev ffmpeg`
  - **Note:** if you are using a different version of python than your distro default, install the correct dev package (e.g.: `python3.8-dev`)
- Enable and start supervisor:
  - **Warning:** on ubuntu 18.04 LTS, the supervisor package only runs when using python2.7 as the default system python version. If necessary, use `sudo update-alternatives --config python`
  ```
  sudo systemctl enable supervisor
  sudo systemctl start supervisor
  ```
- Install gunicorn: `pip install gunicorn`
  - **Note:** if you are using virtualenv, don't forget to enable it **BEFORE** using pip

### Create user
- This user will be used exclusively to run GEN:
- Create user and add it to sudoers list:
```
adduser gen
gpasswd -a gen sudo
```

### PostgreSQL
- Switch to postgres user: `sudo su - postgres`
- Create database user: `createuser u_gen`
- Create a new database and set the user as the owner: `createdb django_gen --owner u_gen`
- Define a strong password for the user: `psql -c "ALTER USER u_gen WITH PASSWORD 'PUT_DB_USER_PASSWORD_HERE'"`
- Exist postgres user: `exit`
- Edit `.env`, uncomment `DATABASE_URL` line and update it with your postgresql server settings (default port is 5432)

### NGINX
- Create `/etc/nginx/sites-available/GEN` with the following content:
```
server {
        listen 80 default_server;
        #server_name gen.test.ca;
        access_log off;
        location /static/ {
                # files that will be gathered by manage.py collecstatic
                alias /opt/GEN_static/;
        }
	location /media/ {
		# media files uploaded by users
		alias /opt/GEN_media/;
	}
        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header X-Forwarded-Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
		client_max_body_size 300M;
        }
}
```
- Create static files directory: `sudo mkdir /opt/GEN_static/`
- Create media files directory: `sudo mkdir /opt/GEN_media/`
- Change ownership of static and media directories to user that will run GEN (e.g., `sudo chown user:usergroup /opt/GEN_static`
- Enable GEN on nginx: `sudo ln -s /etc/nginx/sites-available/GEN /etc/nginx/sites-enabled/GEN`
- Remove default nginx site (if it exists): `sudo rm /etc/nginx/sites-enabled/default`
- Restart service: `sudo service nginx restart`

### UFW (firewall)
- If UFW is enabled:
```
sudo ufw allow http
sudo ufw allow https
```
- To enable UFW: `sudo ufw enable`

### Set up GEN database and superuser (admin)
- Generate database: `python manage.py migrate`
- Create a super user: `python manage.py createsuperuser --username USERNAME --email USER_EMAIL`

### GEN settings
- Edit `GEN/settings.py` and modify the following:
  - add `STATIC_ROOT=/opt/GEN_static/` before `STATIC_URL`
  - change `MEDIA_ROOT` to `/opt/GEN_media/`
- Edit `.env` and set `DEBUG=False`y
- Collect static files: `python manage.py collectstatic`

### Start the server
- Gunicorn: `gunicorn GEN.wsgi`
