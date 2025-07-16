# Period Tracking Job

This project is a FastAPI-based backend server designed for period tracking automation.
## Quick Start

1. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

2. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```
## Features

- RESTful API endpoints for period tracking
- Lightweight and fast performance using FastAPI

## Running the Server

```bash
uvicorn main:app --reload
```

## Setting Up as a Cron Job

To automate requests to your deployed backend, you can use [cron-job.org](https://cron-job.org/) or similar services. Configure the cron job to periodically send HTTP requests to your API endpoint, enabling scheduled tasks without manual intervention.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn

## Installation

```bash
pip install fastapi uvicorn
```

## Example Usage

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/track-period")
def track_period():
    return {"status": "success"}
```
