# Install

## Python

```
$ sudo apt install python2.7
```

## Flask

```
$ sudo apt install python-flask python-flaskext.wtf
$ sudo pip install --upgrade flask-bootstrap
```

## Database

```
$ sudo apt install \
	python-sqlite \
	python-flask-sqlalchemy \
	python-flask-migrate python-flask-script
	
$ sudo pip install --upgrade \
	flask-script flask-migrate
```

```
$ FLASK_APP=httpd.py flask db init
$ FLASK_APP=httpd.py flask db migrate
$ FLASK_APP=httpd.py flask db upgrade
```

### MySQL -> MariaDB

* https://linuxize.com/post/how-to-install-mysql-on-debian-9/
* https://www.linode.com/docs/databases/mariadb/mariadb-setup-debian/

```
$ sudo apt install \
	python-pymysql python-mysqldb \
	mariadb-server mariadb-client mysql-workbench
$ sudo systemctl status mysql
$ sudo mysql_secure_installation
```
```
$ sudo mysql -u root -p

create database PIM;

GRANT ALL PRIVILEGES ON PIM.* TO flask@'127.0.0.1' IDENTIFIED BY 'you-will-never-guess';

FLUSH PRIVILEGES;

quit;

```

```
/etc/mysql/mariadb.conf.d/50-server.cnf

bind-address            = 127.0.0.1
```
