import os
from datetime import datetime
from fastapi import FastAPI

POD_NAME = os.environ['POD_NAME']


# Create an instance of the FastAPI framework
app = FastAPI()
# print("{} - {}".format(POD_NAME, datetime.now().isoformat()))


@app.get("/")
def read_root():
    print("Requested on: {} at: {}".format(
        POD_NAME, datetime.now().isoformat()))
    return {
        "message": "Hello, World! from v6",
        "pod_name": POD_NAME
    }


@app.get("/health")
def health_check():
    return "Ok"
