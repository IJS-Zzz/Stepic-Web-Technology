mysql -u root -e "CREATE DATABASE IF NOT EXISTS stepik CHARACTER SET utf8"
mysql -u root -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'stepik'"
mysql -u root -e "GRANT ALL ON stepik.* TO 'django'@'localhost' IDENTIFIED BY 'stepik'"

# mysql -u root -e "GRANT ALL ON *.* TO 'django'@'localhost' IDENTIFIED BY 'stepik'"