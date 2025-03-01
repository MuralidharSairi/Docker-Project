# Use a small base image
FROM python:3.9-alpine

# Set working directory inside the container
WORKDIR /home

# Copy project files to container
COPY scripts.py /home/scripts.py
COPY data /home/data

# Run script on container start
CMD ["python", "/home/scripts.py"]
