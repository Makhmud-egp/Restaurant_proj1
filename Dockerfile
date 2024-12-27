# Base image
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Install system dependencies for MySQL and PostgreSQL
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    libpq-dev \
    pkg-config \
    && apt-get clean

# Copy requirements.txt into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose the port your app runs on (adjust if necessary)
EXPOSE 8000

# Command to run your application
CMD ["python", "./restaurant_proj/manage.py", "runserver", "0.0.0.0:8000"]
