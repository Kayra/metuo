# metuo

**Photography portfolio site**

Features:

* Shows pictures taken nearest to you first
* No adverts
* Looks hot
* Navigation makes sense


## Development set up

**Requires local installation of [docker-compose.](https://docs.docker.com/compose/install/)**

The Makefile contains useful helper commands for development workflows.

```bash
# Set up and run the application
make install

# Start the application
make start

# Restart the application
make restart

# Create the database on existing server
make database

# Create the dotenv file required by docker-compose
make dotenv

# Connect to the api service via bash
make apibash
```

## API Endpoints

### POST - /upload

Saves static image file, and information (name/tags) to the DB.

Example CURL:

```bash
curl --request POST \
  --url http://127.0.0.1:5000/upload \
  --header 'content-type: multipart/form-data; boundary=---011000010111000001101001' \
  --form tags=hey \
  --form image=path_to_image
```