
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship
from configuracion import cadena_conexion

# Creamos el motor de la base de datos
Engine = create_engine(cadena_conexion)
Base = declarative_base()


class Clinica(Base):
    __tablename__ = 'clinicas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(150), nullable=False)
    responsable = Column(String(100), nullable=False)

    consultorios = relationship(
        "Consultorio",
        back_populates="clinica",
        cascade="all, delete-orphan"
    )


class Consultorio(Base):
    __tablename__ = 'consultorios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)
    clinica_id = Column(Integer, ForeignKey('clinicas.id'), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")

    veterinarios = relationship(
        "Veterinario",
        back_populates="consultorio",
        cascade="all, delete-orphan"
    )


class Veterinario(Base):
    __tablename__ = 'veterinarios'

    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(120), nullable=False, unique=True)
    licencia = Column(String(50), nullable=False, unique=True)

    consultorio_id = Column(
        Integer,
        ForeignKey('consultorios.id'),
        nullable=False
    )

    consultorio = relationship(
        "Consultorio",
        back_populates="veterinarios"
    )

    historias = relationship(
        "HistoriaClinica",
        back_populates="veterinario",
        cascade="all, delete-orphan"
    )


class HistoriaClinica(Base):
    __tablename__ = 'historias_clinicas'

    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    diagnostico = Column(String(200), nullable=False)
    tratamiento = Column(String(200), nullable=False)
    mascota = Column(String(100), nullable=False)

    veterinario_id = Column(
        Integer,
        ForeignKey('veterinarios.id'),
        nullable=False
    )

    veterinario = relationship(
        "Veterinario",
        back_populates="historias"
    )


# Generar físicamente las tablas
Base.metadata.create_all(Engine)

print("Base de datos y tablas creadas con éxito.")
