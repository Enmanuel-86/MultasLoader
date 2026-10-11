from ..conexion_db import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

class Personas(Base):
    __tablename__ = 'personas'

    id_persona: Mapped[int] = mapped_column(Integer, primary_key= True, autoincrement= True)
    cedula: Mapped[String] = mapped_column(String(20), nullable= False)
    nombre: Mapped[String] = mapped_column(String(50), nullable= False)
    apellido: Mapped[String] = mapped_column(String(50), nullable= False)
    residencia: Mapped[String] = mapped_column(String(50), nullable= False)


    def __repr__(self) -> str:
        return f"Id: {self.id_persona} Nombre: {self.nombre}, Apellido: {self.apellido}, Residencia: {self.residencia}"

