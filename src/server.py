from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from infra.sqlalchemy.config.database import create_db, get_db
from schemas import schema
from infra.sqlalchemy.repositories.repo_series import Repo_series



create_db()

app = FastAPI()

@app.post('/series')
def create_serie(serie : schema.Serie, db : Session = Depends(get_db)):
    new_serie = Repo_series(db).create(serie)
    return new_serie

@app.get('/series')
def get_all_series(db : Session = Depends(get_db)):
    series = Repo_series(db).show_all()
    return series

@app.get('/series/{series_id}')
def get_series(series_id : int, db : Session = Depends(get_db)):
    serie = Repo_series(db).get_serie(series_id)
    return serie

@app.delete('/series/{series_id}')
def delete_series(series_id : int, db : Session = Depends(get_db)):
    delete_serie = Repo_series(db).delete(series_id)
    return delete_serie


# cd app-my-flix\src & uvicorn server:app --reload