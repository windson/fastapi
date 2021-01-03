# Deploy FastAPI on Ubuntu and Serve using Caddy 2 Web Server

FastAPI with Async REST API with PostgreSQL on Ubuntu and Serve using Caddy 2 Web Server




Detailed Tutorials on Development & Deployment
- Development: [Implementing Async REST APIs in FastAPI with PostgreSQL CRUD](https://www.tutlinks.com/fastapi-with-postgresql-crud-async/, 'Implementing Async REST APIs in FastAPI with PostgreSQL CRUD')
- Debugging in VS Code: [Debug FastAPI in VS Code IDE](https://bit.ly/3hcXToY, 'Debug FastAPI in VS Code IDE')
- Deployment [Deploy FastAPI on Azure App Service](https://bit.ly/3gPntQ7, 'Deploy FastAPI on Azure App Service')


| Code 💻 | Video 📺 | Article 📝 |
|----------|-------------|------|
| [Deploy FastAPI on GCP](https://github.com/windson/fastapi/tree/fastapi-deploy-google-cloud-platform) | [Deploy FastAPI Python app to Google Cloud Platform on App Engine](https://bit.ly/3g0VwFE) | [Deploy FastAPI app on Google Cloud Platform](https://bit.ly/3axKog8) |
| [Deploying fastapi app to Heroku](https://github.com/windson/fastapi/tree/fastapi-deploy-heroku) | [Deploy FastAPI on Heroku in just 6 minutes](http://bit.ly/3aO1g35) | [Create and Deploy FastAPI app to Heroku](http://bit.ly/2RD68jM) |
| [FastAPI CRUD Async PostgreSQL](https://github.com/windson/fastapi/tree/fastapi-postgresql-azure-deploy) | [Implementing Async REST APIs in Python using FastAPI with PostgreSQL CRUD](https://bit.ly/3j42qvf) | [Implementing Async REST APIs in FastAPI with PostgreSQL CRUD](https://bit.ly/2O6onvp) |
| [Deploy FastAPI on Azure](https://github.com/windson/fastapi/tree/fastapi-postgresql-azure-deploy) | [How to Deploy FastAPI on Azure App Service in just 30 minutes](https://bit.ly/2HA6SUj) | [Deploy FastAPI with CRUD + PostgreSQL on Azure App Service](https://bit.ly/3gPntQ7) |
| [FastAPI CRUD Async PostgreSQL](https://github.com/windson/fastapi/tree/fastapi-postgresql-azure-deploy) | - | [Debug FastAPI in VS Code IDE](https://bit.ly/3hcXToY) |
| [Deploy FastAPI on Ubuntu and Serve using Caddy 2 Web Server](https://github.com/windson/fastapi/tree/fastapi-postgresql-caddy-ubuntu-deploy) | [Deploy FastAPI on Ubuntu (FastAPI + CRUD + PostgreSQL + Gunicorn Systemd + Caddy 2)](https://bit.ly/3hpS0Ws) | [Deploy FastAPI on Ubuntu and Serve using Caddy 2 Web Server](https://bit.ly/2SGLWgt) |


## Setup this Repo on Local PC

In `main.py` comment the following line

```python
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username,db_password, host_server, db_server_port, database_name, ssl_mode)
```

and uncomment the following line

```python
DATABASE_URL = "sqlite:///./test.db"
```

Replace following code

```python
engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=20, max_overflow=0
)
```

with 

```python
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
```


### Windows Users
In command terminal run the following command
```shell
python -m venv env
env/Scripts/activate
python -m pip install -U pip
pip install -r requirements.txt
```

### Install Virtual Environment
In command terminal run the following command
```shell
apt install python3-venv
python3 -m venv env
source ./env/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
```

If you want to use sqlite then install databases module for sqlite as follows

```shell
pip install databases[sqlite]
```

## Run this app on Local PC
In command terminal run the following command
```shell
uvicorn main:app --reload
```


## Deployment command

```shell
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```
