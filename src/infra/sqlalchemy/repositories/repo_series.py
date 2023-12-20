from infra.sqlalchemy.models import model
from schemas import schema
from sqlalchemy.orm import Session
from sqlalchemy import select, delete

class Repo_series():
    def __init__(self, db : Session):
        self.db = db
        
    def create(self, serie : schema.Serie):
        db_serie = model.Series(
            title = serie.title,
            year = serie.year,
            gender = serie.gender,
            seasons = serie.seasons
        )
        
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)
        
        return db_serie
        
    def show_all(self):
        series = self.db.query(model.Series).all()
        return series
        
    def get_serie(self, id_serie : int):
        statement = select(model.Series).filter_by(id=id_serie)
        serie = self.db.execute(statement).one()
        return serie
    
    def delete(self, serie_id : int):
        statement = delete(model.Series).where(model.Series.id == serie_id)
        self.db.execute(statement)
        self.db.commit()

