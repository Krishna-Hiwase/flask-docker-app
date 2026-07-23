# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Expose Flask port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
