# metuo (WIP - live but not v1 yet)

**Photography portfolio site**

Features:

* Shows pictures taken nearest to you first
* No adverts
* Looks hot
* Filtering makes sense

## Wireframe

![wireframe](wireframe.png)

## Development set up

**Requires local installation of [docker-compose](https://docs.docker.com/compose/install/) and [node/npm.](https://www.npmjs.com/get-npm)** 

The Makefile contains common workflow commands and is only used for local development.

### Server installation

From the project root folder, first run the **installation command**:

```bash
make install
```

While the docker container is running, in another shell run the **database creation command**:

```bash
make database
```

### Client installation

### Common workflows

#### Restarting and recreating

#### Testing s3 image uploading

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