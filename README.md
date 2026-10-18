# My Docker Web Application

A small Python web application for Docker practice. It uses Python's built-in HTTP server, so no extra Python packages are needed.

## Requirements
- Docker Desktop installed and running

## Run with Docker Compose
Open a terminal in this folder and run:

```bash
sudo docker compose up --build -d
```

Then open:
- Main page: http://localhost:8000
- Health endpoint: http://localhost:8000/health
- Info endpoint: http://localhost:8000/info

## Useful commands

```bash
sudo docker compose ps
sudo docker compose logs -f
sudo docker compose down
```

If a container named `my-python-container` already exists from earlier practice, remove it first:

```bash
sudo docker rm -f my-python-container
```

Then run `sudo docker compose up --build -d` again.

## Build and run without Compose

```bash
sudo docker build -t my-python-app .
sudo docker run -d -p 8000:8000 --name my-python-container my-python-app
```
