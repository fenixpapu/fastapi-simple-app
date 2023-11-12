from fastapi import FastAPI

# Create an instance of the FastAPI framework
app = FastAPI()

# Define a route that returns "Hello, World!"
@app.get("/")
def read_root():
    return {"message": "Hello, World! from v1"}