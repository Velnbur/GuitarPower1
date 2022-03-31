# GuitarPower

My old unfinished **Django** project. Site like OLX and Avito but for musions
and musical instruments master. One of my first big apps

## Prerequisites 

- python >= 3.8

## Install and use

Clone repository:
```shell
$ git clone git@github.com:Velnbur/GuitarPower1 && cd GuitarPower1
```

Create virtual environment:
```shell
$ mkdir env && python3 -m venv ./env
```

Activate it:
```shell
$ source ./env/bin/activate
```

Install requirments:
```shell
$ pip3 install -r ./requirments.txt
```

Create sqlite DB and make migrations:
```shell
$ touch app/db.sqlite3  
$ python3 app/manage.py migrate  
$ python3 app/manage.py makemigrations  
```

Run server:
```shell
$ python3 app/manage.py runserver 8000
```

## Contributors

- [@Velnbur](https://github.com/Velnbur)
- [@OmegaTymbJIep](https://github.com/OmegaTymbJIep)
