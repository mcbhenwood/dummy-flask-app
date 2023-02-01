# dummy-flask-app

Simple 'Hello World' style app to give something to deploy.

## Build

```bash
docker build -t dummy .
```

### Run

```bash
docker run -p "8080:80" -e "FOREIGN_SERVICE_URL=SOMEURL" dummy
```

Go to <http://localhost:8080> in your browser.

To access the URL which consumes some other service, be sure to specify a valid `FOREIGN_SERVICE_URL` as per the `docker run` instruction above, then go in your browser to <http://localhost:8080/retrieve_other_service_content>.