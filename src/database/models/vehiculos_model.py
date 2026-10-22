from ..conexion_db import Base
from typing import List
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CatalogoTiposVehiculos(Base):
    __tablename__ = 'catalogo_tipos_vehiculos'

    id_tipo: Mapped[int] = mapped_column(Integer, primary_key= True, autoincrement= True)
    tipo: Mapped[String] = mapped_column(String(30), nullable= False)
    vehiculo: Mapped[List["Vehiculos"]] = relationship(back_populates="tipo")

    def __repr__(self) -> str:
        return f"Id: {self.id_tipo} Marca: {self.tipo}"


class CatalogoModelosVehiculos(Base):
    __tablename__ = 'catalogo_modelos_vehiculos'

    id_modelo: Mapped[int] = mapped_column(Integer, primary_key= True, autoincrement= True)
    modelo: Mapped[String] = mapped_column(String(30), nullable= False)

    vehiculo: Mapped[List["Vehiculos"]] = relationship(back_populates="modelo")


    def __repr__(self) -> str:
        return f"Id: {self.id_modelo} Marca: {self.modelo}"



class CatalogoMarcasVehiculos(Base):
    __tablename__ = 'catalogo_marcas_vehiculos'

    id_marca: Mapped[int] = mapped_column(Integer, primary_key= True, autoincrement= True)
    marca: Mapped[String] = mapped_column(String(30), nullable= False)

    vehiculo: Mapped[List["Vehiculos"]] = relationship(back_populates="marca")

    def __repr__(self) -> str:
        return f"Id: {self.id_marca} Marca: {self.marca}"






class Vehiculos(Base):
    __tablename__ = 'vehiculos'

    id_vehiculo: Mapped[int] = mapped_column(Integer, primary_key= True, autoincrement= True)
    id_tipo: Mapped[int] = mapped_column(ForeignKey("catalogo_tipos_vehiculos.id_tipo"))
    id_modelo: Mapped[int] = mapped_column(ForeignKey("catalogo_modelos_vehiculos.id_modelo"))
    id_marca: Mapped[int] = mapped_column(ForeignKey("catalogo_marcas_vehiculos.id_marca"))
    tipo: Mapped["CatalogoTiposVehiculos"] = relationship(back_populates="vehiculo")
    modelo: Mapped["CatalogoModelosVehiculos"] = relationship(back_populates="vehiculo")
    marca: Mapped["CatalogoMarcasVehiculos"] = relationship(back_populates="vehiculo")

    placa: Mapped[str] = mapped_column(String(20), unique= True)
    color: Mapped[str] = mapped_column(String(50))

 
    def __repr__(self) -> str:
        return f"Id: {self.id_vehiculo} id_tipo: {self.id_tipo}, id_modelo: {self.id_modelo}, id_marca: {self.id_marca}, placa: {self.placa}, color: {self.color}"







