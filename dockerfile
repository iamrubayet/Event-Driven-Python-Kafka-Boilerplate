# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies required by the project
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 9092 (Kafka default) if needed for external communication
EXPOSE 9092

# Copy the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Use the entrypoint script to run all the Python scripts
ENTRYPOINT ["/app/entrypoint.sh"]
