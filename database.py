from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = "mysql+pymysql://root:Anil@2167@localhost:3306/fastapi_db"
DATABASE_URL = "mysql+pymysql://root:Anil%402167@localhost:3306/fastapi_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()