from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLDB_URL = 'sqlite:///./itproger.db'
engine = create_engine(SQLDB_URL, connect_args={'check_same_thread': True})

session_local = sessionmaker(autoflush=False, autocommit=False)
Base = declarative_base()