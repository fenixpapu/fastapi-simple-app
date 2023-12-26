import os
from datetime import datetime
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Session

POD_NAME = os.environ['POD_NAME']
POSTGRESQL_URI = os.environ['POSTGRESQL_URI']


# Create an instance of the FastAPI framework
app = FastAPI()
# print("{} - {}".format(POD_NAME, datetime.now().isoformat()))

# Database configuration
DATABASE_URL = "postgresql://postgres:password@{}/kolyde".format(
    POSTGRESQL_URI)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def check_db_connection(db: Session = Depends(lambda: SessionLocal())):
    try:
        db.execute("SELECT 1")
        return db
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Unable to connect to the database: {str(e)}")
    finally:
        db.close()


@app.get("/")
def read_root(db: Session = Depends(check_db_connection)):
    print("Requested on: {} at: {}".format(
        POD_NAME, datetime.now().isoformat()))

    return {
        "message": "Hello, World! from v6",
        "pod_name": POD_NAME,
        "connect_db": "success"
    }


@app.get("/health")
def health_check():
    return "Ok"
