# Python to test argoCD :D

- To activate venv: `source venv/bin/activate`

- To install requirements package: `pip3 install -r requirements.txt`

- To start server: `POD_NAME="test" POSTGRESQL_URI='localhost' uvicorn main:app --reload`. And access: `http://localhost:8000`

## Docker guide

- Build with command:

```
docker buildx build --platform linux/amd64 -t fenixpapu/fastapi-simple-app:v9 .
```

- Push images to cloud:

```
docker push fenixpapu/fastapi-simple-app:v9
```

- Or push to private repo:

```
# create new tag from exist tag
docker tag fenixpapu/fastapi-simple-app:v9 fenixpapu/private-fastapi-simple-app:v9
# push to private repo:
docker push fenixpapu/private-fastapi-simple-app:v9
```

- Run on local:

```
docker run -d -p 80:80 fenixpapu/fastapi-simple-app:v9
```
