# lettergun-server

This FastAPI server exposes an endpoint (the "webapp endpoint") which the
lettergun webapp can contact to initiate letter writing.

The FastAPI app validates the webapp's JSON payload, then sends it to
the `lettergun-handwriting` app. If the payload is valid it returns an `200` response.

`lettergun-handwriting` parses the JSON to create an svg image of the
handwritten note. It sends the image to the image endpoint on the API
server.

The API server verifies the SVG image against the original JSON payload and if
it is valid, used the AxiDraw Python API to plot the SVG image. When the image
is complete, it notifies the API server, which notifies the webapp.

## Documentation

- [http://127.0.0.1/docs](http://127.0.0.1/docs)
- [http://127.0.0.1/redoc](http://127.0.0.1/redoc)


## Docker

Use the following command whilst developing to build and run a docker image
based on current code:

`docker stop container-one && docker rm container-one && docker build -t
image-one . && docker run -d --name container-one -p 80:80 image-one`

To shell into it and run the tests:

`docker exec -it container-one pytest app/`

## Running locally

Once the container is running, and assuming you've mapped the ports to `80:80`,
you can go to [http://127.0.0.1/](http://127.0.0.1/).

You can experiment with API requests by using `httpie`. Use the command `https
http://127.0.0.1` to get started. 

`http post http://127.0.0.1/api/v1/create/ uid=foo message="Dear {name}, Good bye." "variables[0][name]=Joe" "variables[0][product]=tshirt" paper_size=A6 paper_orientation=landscape paper_type=p1`

## Testing

To run the test suite: `docker exec -it container-one pytest app/`
