# Use the official Python image as the base image
FROM python:3.9

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the FastAPI application code into the container
COPY main.py .

# Expose the port the application will run on
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]