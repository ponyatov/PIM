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
```