from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión: postgresql://usuario:password@host:puerto/nombre_db
sqlalchemy_database_url = "postgresql://user_admin:password123@localhost:5432/inventory_db"

# El engine es el encargado de la comunicacion fisica con la DB
engine = create_engine(sqlalchemy_database_url)

# La sesion es lo que usaremnos para hacer consultas
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para crear nuestros modelos (Tablas)
Base = declarative_base()

# Dependencia para obtener la DB en nuestras rutas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db_close()
