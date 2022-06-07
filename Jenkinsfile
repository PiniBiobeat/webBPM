# Build Environment: Playwright
FROM mcr.microsoft.com/playwright/python:v1.21.0-focal

# Add python script to Docker
COPY pytest test_online_create_album.py /

# Run Python script
CMD [ "python", "pytest test_online_create_album.py" ]