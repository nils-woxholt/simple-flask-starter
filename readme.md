# Instructions

## Python environment

```bash
python -m venv .venv
# or
python3 -m venv .venv
```

## Install dependencies

```bash
pip install -r ./app/requirements.txt
```

## Run flask locally

```bash
FLASK_APP=app
flask run
```

Now you can browse to <http://localhost:5000/>

If you have the Visual Studio Code REST Client extension installed, you can open test.http and click on the various endpoints to test.

## Docker commands

```bash
# build the container
docker build -t my-model .

# run the container
docker run -p 5000:5000 my-model

# optionally run via docker-compose
docker-compose up
```
