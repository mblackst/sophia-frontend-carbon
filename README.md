# Sophia Patient Dashboard (With Login)

## Features

- Login page based on provided design
- Background extracted from screenshot
- Redirect to patient list after login
- Fully containerized (Dockerfile included)
- Ready for OpenShift deployment

## Default Credentials

- Username: admin
- Password: password

## Local Testing

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Build Docker Image

```bash
podman build -t patient-dashboard:latest .
```

## Deploy to OpenShift

Use the same podman tagging and pushing process we discussed earlier.

Enjoy!
