FROM mcr.microsoft.com/playwright/python:v1.57.0-noble

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y xvfb

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Use xvfb-run to simulate a display server
CMD ["xvfb-run", "--auto-servernum", "--server-args=-screen 0 1280x720x24", "pytest", "-vv", "-s"]