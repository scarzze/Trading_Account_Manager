#our database setup script and alembic for migrations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///trading.db"

engine = create_engine(DATABASE_URL,echo=True)
Session= sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

if __name__ =="__main__":
    init_db()
    print("succesfully initialized the database")
