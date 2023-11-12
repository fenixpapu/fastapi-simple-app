import os
from fastapi import FastAPI

POD_NAME = os.environ['POD_NAME']

# Create an instance of the FastAPI framework
app = FastAPI()

# Define a route that returns "Hello, World!"


@app.get("/")
def read_root():
    return {
        "message": "Hello, World! from v3",
        "pod_name": POD_NAME
    }


@app.get("/health")
def health_check():
    return "Ok"
