# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the entry point (run the script)
ENTRYPOINT ["python", "translate.py"]
