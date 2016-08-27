# INSTALL DEPENDENCIES
# -----------------------------------------------------------------------------
sudo apt-get install python3-picamera
sudo apt-get install python3-pip
sudo pip install virtualenv

sudo apt-get install libapache2-mod-wsgi
# -----------------------------------------------------------------------------


# CREATE VIRTUAL ENVIRONMENT 
# -----------------------------------------------------------------------------
sudo virtualenv venv
source venv/bin/activate
sudo pip install -r requirements.txt
# -----------------------------------------------------------------------------


# CLONE SOURCE
# -----------------------------------------------------------------------------
cd /var/www
sudo git pull https://github.com/asbarber/personal-website app
# -----------------------------------------------------------------------------


# ADD HOST
# -----------------------------------------------------------------------------
sudo vim /etc/hosts
# add the line:
#	127.0.1.1    98.224.222.230    app
# -----------------------------------------------------------------------------


# ADD VIRTUAL HOST
# -----------------------------------------------------------------------------
sudo vim /etc/apache2/app.conf
# add the lines:
#	<VirtualHost *>
#	 ServerName 98.224.222.230
#
#	 WSGIDaemonProcess app user=pi group=pi threads=5
#	 WSGIScriptAlias / /var/www/app/app.wsgi
#
#	<Directory /var/www/app/>
#	 WSGIProcessGroup app
#	 WSGIApplicationGroup %{GLOBAL}
#	 WSGIScriptReloading On
#
#	 Require all granted
#	</Directory>
#	</VirtualHost>
# -----------------------------------------------------------------------------


# ENABLE SITES
# -----------------------------------------------------------------------------
# disable other sites (e.g. the default)
# sudo a2dissite 000-default.conf 
sudo a2ensite app.conf 
# -----------------------------------------------------------------------------


# RESTART APACHE
# -----------------------------------------------------------------------------
sudo service apache2 restart
# -----------------------------------------------------------------------------
