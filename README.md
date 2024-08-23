# Project README

## Overview

This project consists of a multi-service application that includes a backend, a MySQL database, a PhpMyAdmin interface, and Chroma for data indexing. The Docker Compose configuration manages the entire setup, making it easy to run and maintain.

## Services

### Backend

- **Directory**: `./backend`
- **Port**: `4000:4000`
- **Environment**: Loaded from `.env` file
- **Description**: The backend service is built from the local `./backend` directory. It exposes port 4000 for communication with other services or external clients.

### Database (MySQL)

- **Image**: `mysql`
- **Port**: (No external port exposed)
- **Volumes**:
  - Local file `./database/init.sql` is mounted to the container at `/data/application/init.sql`.
- **Command**: The MySQL server is initialized with a custom SQL file (`init.sql`).
- **Restart Policy**: Always
- **Description**: This service runs a MySQL database instance and initializes it with a custom SQL file located in `./database/init.sql`.

### PhpMyAdmin

- **Image**: `phpmyadmin`
- **Port**: `8081:80`
- **Environment Variables**:
  - `PMA_ARBITRARY=1`
- **Restart Policy**: Always
- **Description**: PhpMyAdmin is used to interact with the MySQL database via a web interface, accessible on `http://localhost:8081`.

### Chroma

- **Image**: `ghcr.io/chroma-core/chroma:latest`
- **Port**: `8000:8000`
- **Volumes**:
  - `index_data:/chroma/.chroma/index`
- **Description**: Chroma is used for data indexing. The indexed data is stored in a Docker volume called `index_data`.

## Volumes

### index_data
- **Driver**: Local
- **Description**: Persists the data indexed by Chroma.

### backups
- **Driver**: Local
- **Description**: (Add description if this volume is used somewhere in your setup, otherwise you may want to remove it from the configuration).

## Getting Started

### Prerequisites

- create a .env file in which we store the API key and any other env variable used on containers

- Docker and Docker Compose installed on your machine.

#### Commands to Start/Stop:
```bash
# build the backend service
docker-compose build backend
# Start the backend service
docker-compose up backend