from pydantic import BaseModel


class AnalystBase(BaseModel):
    """Analyst base para la carga (lo que se solicita en el post)

    Args:
        BaseModel (_type_): _description_
    """
    name: str
    is_admin: bool = None


class AnalystCreate(AnalystBase):
    """Utilizado para la creación

    Args:
        AnalystBase (_type_): _description_
    """
    pass


class Analyst(AnalystBase):
    """
    El modelo completo
    """
    id: str
    unique_id: str


    class Config:
        orm_mode = True