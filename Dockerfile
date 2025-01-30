FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install Java (required for VnCoreNLP)
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create directory for VnCoreNLP model
RUN mkdir -p /app/vncorenlp

# Create directory for logs
RUN mkdir -p /app/logs

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    FLASK_APP=text_segmentation/app.py

# Expose port
EXPOSE 5000

# Command to run the application
CMD ["python", "run.py"]
