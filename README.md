# metuo

**Photography portfolio site**

Features:

* Shows pictures taken nearest to you first
* No adverts
* Looks  a e s t h e t i c
* Filtering makes sense (to me)

## Wireframe

![wireframe](wireframe.png)

## Todo

- [ ] Refactor server
- [ ] Refactor client
- [ ] Add server tests
- [ ] Add client tests
- [ ] Add mobile styles
- [ ] Create upload page
- [ ] Create archive page

## Development set up

**Requires local installation of [docker-compose](https://docs.docker.com/compose/install/) and [node/npm.](https://www.npmjs.com/get-npm)** 

The Makefile contains common workflow commands and is only used for local development.

### Server installation and start up

From the project root folder, first run the **installation command**:

```bash
make install
```

While the docker container is running, in another shell run the **database creation command**:

```bash
make database
```

This will create the required docker images and run their containers for the `api server` and the `postgres database`. 

To simply start this environment in the future run the **start command**:

```bash
make start
```

**The server should be accessible at `http://0.0.0.0:5000/`**

### Client installation and start up

Navigate to the `client` directory, and **install the node modules**:

```bash
cd client
npm ci
```

Once the node modules have been installed, **start the client development server**:

```bash
npm run start
```

**The client should be accessible at `http://0.0.0.0:3000/`**

### Common workflows

#### Rebuilding the api server

To rebuild and restart the flask api server **run the restart command**:

```bash
make restart
```

#### Recreating the development environment

To recreate the development environment from scratch, **first remove the `postgres-data` directory and it's contents**:

```bash
rm -rf postgres-data
```

Then **remove the docker images**:

```bash
> docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
metuo_server        latest              377b22651d7d        18 hours ago        1.02GB
postgres            alpine              ecb176ff304a        2 weeks ago         151MB
python              3.7                 f66befd33669        6 weeks ago         919MB
> docker rmi -f 377b22651d7d ecb176ff304a f66befd33669
```

Then run the **installation command**:

```bash
make install
```

Finally, while the docker container is running, in another shell run the **database creation command**:

```bash
make database
```

#### Testing s3 image uploading

To save images to s3 from the development environment rather than locally, **change the following environment variables in the `.env` file**:

* `IMAGE_DIRECTORY` - Change this to the bucket name
* `AWS_ACCESS_KEY_ID` - Update this with a key ID that is authorised to interact with the bucket
* `AWS_SECRET_ACCESS_KEY` - Update this with a key secret that is authorised to interact with the bucket
* `FLASK_DEBUG` - Change this to `0` (alternatively, change all references in the code to expect this to be `1` to keep development debug messages and behaviours, **but do not commit this change**)

Then **restart the server docker container**:

```bash
make restart
```

#### Environment introspection

The `Makefile` provides quick and easy access to the server and database:

* `make servershell` creates an interactive terminal in the running api docker container
* `make psqlshell` creates a connection to the api database

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