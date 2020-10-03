# Deploy FastAPI on Azure

FastAPI with Async REST API with PostgreSQL on Azure App Service 

Detailed Tutorials on Development & Deployment
- Development: [Implementing Async REST APIs in FastAPI with PostgreSQL CRUD](https://www.tutlinks.com/fastapi-with-postgresql-crud-async/, 'Implementing Async REST APIs in FastAPI with PostgreSQL CRUD')
- Debugging in VS Code: [Debug FastAPI in VS Code IDE](https://bit.ly/3hcXToY, 'Debug FastAPI in VS Code IDE')
- Deployment [Deploy FastAPI on Azure App Service](https://bit.ly/3gPntQ7, 'Deploy FastAPI on Azure App Service')



|  Article 📝 | Video 📺 | Code 💻 |
|----------|-------------|------|
| [Implementing Async REST APIs in FastAPI with PostgreSQL CRUD](https://bit.ly/2O6onvp) | [Implementing Async REST APIs in Python using FastAPI with PostgreSQL CRUD](https://bit.ly/3j42qvf) | [FastAPI CRUD Async PostgreSQL](https://github.com/windson/fastapi/tree/fastapi-postgresql-azure-deploy) |
| [Deploy FastAPI with CRUD + PostgreSQL on Azure App Service](https://bit.ly/3gPntQ7) | [How to Deploy FastAPI on Azure App Service in just 30 minutes](https://bit.ly/2HA6SUj) | [Deploy FastAPI on Azure](https://github.com/windson/fastapi/tree/fastapi-postgresql-azure-deploy) |
| [Debug FastAPI in VS Code IDE](https://bit.ly/3hcXToY) | - | [FastAPI CRUD Async PostgreSQL](https://github.com/windson/fastapi/tree/fastapi-postgresql-azure-deploy) |


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

### CentOS Users Setup PIP3 and Virtual Environment
In command terminal run the following command
```shell
apt install python3-venv
python3 -m venv env
source ./env/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
```

### Ubuntu Users Setup PIP3 and Virtual Environment
In command terminal run the following command
```shell
sudo apt install python3-pip
sudo pip3 install virtualenv
virtualenv env
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
