from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connect to our pg db
engine=create_engine("postgresql://admin:mvj8Mu9RRMgHjB7n5MPWSjc0ahvqGy4A@dpg-cm1d0igcmk4c73d8kbs0-a.frankfurt-postgres.render.com/blogs_8im4")


# Create connection with sessionmaker
SessionLocal = sessionmaker(bind=engine)

# def method to get db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()