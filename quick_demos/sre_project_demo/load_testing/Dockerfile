# Use an official Python image as the base
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /load_testing

# Copy Locust requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Locust test script
COPY locustfile.py .

# Expose Locust ports (8089 for Web UI, 5557 for workers)
EXPOSE 8089 5557

# Command to run Locust
CMD ["locust"]
