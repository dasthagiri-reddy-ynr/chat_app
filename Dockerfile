# Use an official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the port (Fly default port is 8080)
ENV PORT=8080
EXPOSE 8080

# Start the app with Gunicorn + WebSocket support (eventlet or gevent)
CMD ["gunicorn", "app:app", "--worker-class", "eventlet", "-w", "1", "--bind", "0.0.0.0:8080"]
