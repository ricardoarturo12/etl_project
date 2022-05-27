from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


from . import crud, models, schemas
from .database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/analyst/", response_model=schemas.Analyst)
def post_analyst(analyst: schemas.AnalystCreate, db: Session = Depends(get_db)):
    return crud.create_analyst(db=db, analyst=analyst)


@app.get("/api/analyst/{name}", response_model=schemas.Analyst)
def get_analyst(name:str, db: Session = Depends(get_db)):
    analysts = crud.get_analyst(db, name=name)
    if analysts is None:
        raise HTTPException(status_code=404, detail="Analyst not found")
    return analysts


@app.get("/api/analysts/", response_model=List[schemas.Analyst])
def get_analysts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    analysts = crud.get_analysts(db, skip=skip, limit=limit)
    return analysts


@app.delete("/api/analyst/{name}" )
def delete_analyst(name:str, db: Session = Depends(get_db)):
    response = crud.delete_analyst(db, name=name)
    return response