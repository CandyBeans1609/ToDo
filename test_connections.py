from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:Postgres%40123@localhost:5432/todo_db"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect():
        print("✅ Connected!")
except Exception as e:
    print(e)