from sqlalchemy import Boolean, Column, String


from .database import Base



class Analyst(Base):
    __tablename__ = "analysts"

    id = Column(String, primary_key=True, index=True)
    unique_id = Column(String, index=True)
    name = Column(String, index=True)
    is_admin = Column(Boolean, index=True)

