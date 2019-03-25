# metuo (WIP - not yet live)

**Photography portfolio site**

Features:

* Shows pictures taken nearest to you first
* No adverts
* Looks hot
* Navigation makes sense

## Wireframe

![wireframe](wireframe.png)

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

# Create the database on existing server (can be used to dump and recreate the db)
make database

# Create the dotenv file required by docker-compose
make dotenv

# Connect to the api service via bash
make servershell

# Connect to the database via psql
make psqlshell

# Run unit tests
make testunit

# Run integration tests
make testinteg

# Run end-to-end tests
make e2e

# Run all tests
make testall
```

## Server API Endpoints

### GET - /

Returns `Alive`. Simple health check

Example CURL:

```bash
curl --request GET \
  --url http://0.0.0.0:5000/
```

### GET - /images

Get a list of images. Response will include file name, static serving location and tags.

Example CURL:

```bash
curl --request GET \
  --url 'http://0.0.0.0:5000/images?tags=hey'
```

Example response:

```bash
{
  "nyc.png": {
    "location": "/static/nyc.png",
    "tags": [
      "hey"
    ]
  }
}
```

### GET - /tags

Get a list of all the tags in the DB

Example CURL:

```bash
curl --request GET \
  --url http://0.0.0.0:5000/tags
```

Example response:

```bash
[
  "hey"
]
```

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