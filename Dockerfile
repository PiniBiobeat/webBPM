FROM mcr.microsoft.com/playwright/python:v1.57.0-noble

WORKDIR /app

RUN apt-get update && apt-get install -y xvfb && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [
  "xvfb-run",
  "--auto-servernum",
  "--server-args=-screen 0 1280x720x24",
  "pytest",
  "-vv",
  "--headed",
  "--alluredir=/app/allure-results",
  "--tracing=retain-on-failure",
  "--video=retain-on-failure",
  "--screenshot=only-on-failure"
]
