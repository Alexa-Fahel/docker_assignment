# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy script
COPY consumer.py .

# Create volume directory
VOLUME /data

# Run the script
CMD ["python", "consumer.py"]
