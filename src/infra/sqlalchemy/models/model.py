from infra.sqlalchemy.config.database import Base
from sqlalchemy import Column, String, Integer

class Series(Base):
    __tablename__ = 'series'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    year = Column(Integer)
    gender = Column(String)
    seasons = Column(Integer)