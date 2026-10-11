import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

# 1. Cargar variables del archivo .env
load_dotenv()

# 2. Construir la URL de conexión
# Formato: mysql+driver://usuario:password@host:puerto/base_de_datos
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 3. Crear el Motor (Engine)
# pool_pre_ping=True verifica si la conexión sigue viva antes de lanzar una consulta
# echo=True imprime en consola las consultas SQL (útil para desarrollo, cambiar a False en producción)
engine = create_engine(
    DATABASE_URL, 
    pool_pre_ping=True, 
    echo=False
)


Session= sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()


class Base(DeclarativeBase):
    pass


