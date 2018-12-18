# Comands for fast servers config

# Nginx
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# Gunicorn
sudo ln -sf /home/box/web/etc/gunicorn_config.py  /etc/gunicorn.d/config.py
sudo /etc/init.d/gunicorn restart
# Run Gunicorn in shell for start with config file
#--> gunicorn -c /etc/gunicorn.d/config.py hello:app

# MySQL
sudo /etc/init.d/mysql start
