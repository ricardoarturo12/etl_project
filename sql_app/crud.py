from sqlalchemy.orm import Session


from . import models, schemas
import uuid


def create_analyst(db: Session, analyst: schemas.AnalystCreate):
    unique_id = str(uuid.uuid4())
    db_analyst = models.Analyst(id=unique_id, unique_id=unique_id, name=analyst.name, is_admin=analyst.is_admin)
    db.add(db_analyst)
    db.commit()
    db.refresh(db_analyst)
    return db_analyst


def get_analyst(db: Session, name: str):
    return db.query(models.Analyst).filter(models.Analyst.name == name).first()


def get_analysts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Analyst).offset(skip).limit(limit).all()


def delete_analyst(db: Session, name: str):
    analyst = db.query(models.Analyst).filter(models.Analyst.name == name).first()
    if analyst:
        db.delete(analyst)
        db.commit()
        db.refresh(analyst)
        return {"message": f"Analyst deleted success!"}
    return {"message": f"Analyst not found"}