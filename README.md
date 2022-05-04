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
