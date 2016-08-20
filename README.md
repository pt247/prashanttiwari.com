# prashanttiwari.com
My personal website https://prashanttiwari.com

sudo apt-get install postgresql-client
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql postgres
set password with command '\password postgres'
sudo -u postgres createdb pt_db

sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
pip install psycopg2
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
/etc/rc.local
sudo apt install upstart
(venv) prashant@prashanttiwari:~/prashanttiwari.com/website$ cat  emperor.uwsgi.service
[Unit]
Description=uWSGI Emperor
After=syslog.target

[Service]
ExecStart=/usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --daemonize /var/log/uwsgi-emperor.log
RuntimeDirectory=uwsgi
Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all

[Install]
WantedBy=multi-user.target
(venv) prashant@prashanttiwari:~/prashanttiwari.com/website$ 

