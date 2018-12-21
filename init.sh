# Comands for fast servers config

# Nginx
sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# Correct way to config Gunicorn app
sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart

# Gunicorn
# sudo ln -sf /home/box/web/etc/gunicorn_config.py  /etc/gunicorn.d/config.py
# sudo /etc/init.d/gunicorn restart
# Run Gunicorn in shell for start with config file
#--> gunicorn -c /etc/gunicorn.d/config.py hello:app

# MySQL
sudo /etc/init.d/mysql start

# config DB for work with django
mysql -u root -e "CREATE DATABASE IF NOT EXISTS stepik CHARACTER SET utf8"
mysql -u root -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'stepik'"
mysql -u root -e "GRANT ALL ON stepik.* TO 'django'@'localhost' IDENTIFIED BY 'stepik'"