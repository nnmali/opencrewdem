# OpenCrew

OpenCrew is a simple Flask REST API project.

## Features

- Welcome endpoint
- Health check endpoint
- Get team members
- Add team members
- Automated tests with pytest

## Requirements

- Python 3.12+
- pip

## Installation

```bash
python -m venv .venv
```

Activate the virtual environment, then install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the application

```bash
python app.py
```

The application runs at http://127.0.0.1:5000.

## Run tests

```bash
pytest
```

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| GET | `/team` | Get team members |
| POST | `/team` | Add a team member |
