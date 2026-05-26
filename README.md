# Todo Application

A simple Todo API built with FastAPI, SQLAlchemy, and SQLite.

## Project Structure

```text
├── app/
│   ├── main.py          # FastAPI application entrypoint and routes
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic schemas for data validation
│   └── database.py      # Database connection and session management
│
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup and Running

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```
