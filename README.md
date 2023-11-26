# Python to test argoCD :D

- To activate venv: `source venv/bin/activate`

- To install requirements package: `pip3 install -r requirements.txt`

- To start server: `POD_NAME="test" uvicorn main:app --reload`. And access: `http://localhost:8000`

## Docker guide

- Build with command:

```
docker buildx build --platform linux/amd64 -t fenixpapu/fastapi-simple-app:v5 .
```

- Push images to cloud:

```
docker push fenixpapu/fastapi-simple-app:v5
```

- Run on local:

```
docker run -d -p 80:80 fenixpapu/fastapi-simple-app:v5
```
