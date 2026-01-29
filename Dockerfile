FROM mcr.microsoft.com/playwright/python:v1.57.0-noble

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p artifacts/videos artifacts/traces

CMD bash -lc 'if [ "$HEADED" = "true" ]; then \
               xvfb-run -a pytest; \
             else \
               pytest; \
             fi'
