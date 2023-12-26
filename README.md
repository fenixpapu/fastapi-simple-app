# Python to test argoCD :D

- To activate venv: `source venv/bin/activate`

- To install requirements package: `pip3 install -r requirements.txt`

- To start server: `POD_NAME="test" POSTGRESQL_URI='localhost' uvicorn main:app --reload`. And access: `http://localhost:8000`

## Docker guide

- Build with command:

```
docker buildx build --platform linux/amd64 -t fenixpapu/fastapi-simple-app:v7 .
```

- Push images to cloud:

```
docker push fenixpapu/fastapi-simple-app:v7
```

- Or push to private repo:

```
# create new tag from exist tag
docker tag fenixpapu/fastapi-simple-app:v7 fenixpapu/fastapi-simple-app-private:v7
# push to private repo:
docker push fenixpapu/fastapi-simple-app-private:v7
```

- Run on local:

```
docker run -d -p 80:80 fenixpapu/fastapi-simple-app:v7
```
