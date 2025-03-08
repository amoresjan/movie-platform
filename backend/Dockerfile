# Use official Python image as base
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Start the Django server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
