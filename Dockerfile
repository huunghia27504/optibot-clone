# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY main.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create data folder to store scraped markdown
RUN mkdir -p data

# Default command to run script
CMD ["python", "main.py"]
