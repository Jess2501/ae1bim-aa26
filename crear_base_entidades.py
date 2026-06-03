from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from configuracion import cadena_conexion

# Creamos el motor de la base de datos
Engine = create_engine(cadena_conexion)
Base = declarative_base()

class Facultad(Base):
    __tablename__ = 'facultades'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(150), nullable=False)
    decano = Column(String(100), nullable=False)
    
    carreras = relationship("Carrera", back_populates="facultad", cascade="all, delete-orphan")

class Carrera(Base):
    __tablename__ = 'carreras'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(20), nullable=False, unique=True)
    facultad_id = Column(Integer, ForeignKey('facultades.id'), nullable=False)
    
    facultad = relationship("Facultad", back_populates="carreras")
    profesores = relationship("Profesor", back_populates="carrera", cascade="all, delete-orphan")
    recursos = relationship("RecursoAcademico", back_populates="carrera", cascade="all, delete-orphan")

class Profesor(Base):
    __tablename__ = 'profesores'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False)
    carrera_id = Column(Integer, ForeignKey('carreras.id'), nullable=False)
    
    carrera = relationship("Carrera", back_populates="profesores")

class RecursoAcademico(Base):
    __tablename__ = 'recursos_academicos'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    tipo = Column(String(50), nullable=False)
    url = Column(String(200), nullable=False)
    carrera_id = Column(Integer, ForeignKey('carreras.id'), nullable=False)
    
    carrera = relationship("Carrera", back_populates="recursos")

# Generar físicamente las tablas
Base.metadata.create_all(Engine)
print("Base de datos y tablas creadas con éxito.")