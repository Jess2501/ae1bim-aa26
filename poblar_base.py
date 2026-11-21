
from datetime import date
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import (
    Engine,
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica
)

# Crear sesión
Session = sessionmaker(bind=Engine)
session = Session()

try:
    # Crear clínicas
    clinica1 = Clinica(
        nombre="Veterinaria San Francisco",
        direccion="Av. Principal, Guayaquil",
        responsable="Dr. Carlos Mendoza"
    )

    clinica2 = Clinica(
        nombre="Clinica Huellitas",
        direccion="Av. Amazonas, Quito",
        responsable="Dra. Maria Torres"
    )

    # Crear consultorios
    consultorio1 = Consultorio(
        nombre="Consultorio 1",
        especialidad="Medicina General",
        clinica=clinica1
    )

    consultorio2 = Consultorio(
        nombre="Consultorio 2",
        especialidad="Cirugia",
        clinica=clinica1
    )

    consultorio3 = Consultorio(
        nombre="Consultorio 1",
        especialidad="Dermatologia",
        clinica=clinica2
    )

    # Crear veterinarios
    veterinario1 = Veterinario(
        nombres="Juan",
        apellidos="Perez",
        correo="juan@gmail.com",
        licencia="VET001",
        consultorio=consultorio1
    )

    veterinario2 = Veterinario(
        nombres="Ana",
        apellidos="Lopez",
        correo="ana@gmail.com",
        licencia="VET002",
        consultorio=consultorio2
    )

    veterinario3 = Veterinario(
        nombres="Pedro",
        apellidos="Gomez",
        correo="pedro@gmail.com",
        licencia="VET003",
        consultorio=consultorio3
    )

    # Crear historias clínicas
    historia1 = HistoriaClinica(
        fecha=date(2026, 11, 10),
        diagnostico="Gastroenteritis",
        tratamiento="Medicamentos y dieta especial",
        mascota="Max",
        veterinario=veterinario1
    )

    historia2 = HistoriaClinica(
        fecha=date(2026, 11, 12),
        diagnostico="Infeccion de piel",
        tratamiento="Antibioticos",
        mascota="Luna",
        veterinario=veterinario1
    )

    historia3 = HistoriaClinica(
        fecha=date(2026, 11, 14),
        diagnostico="Fractura",
        tratamiento="Inmovilizacion",
        mascota="Rocky",
        veterinario=veterinario2
    )

    historia4 = HistoriaClinica(
        fecha=date(2026, 11, 15),
        diagnostico="Dermatitis",
        tratamiento="Tratamiento topico",
        mascota="Milo",
        veterinario=veterinario3
    )

    # Guardar todos los registros
    session.add_all([
        clinica1, clinica2,
        consultorio1, consultorio2, consultorio3,
        veterinario1, veterinario2, veterinario3,
        historia1, historia2, historia3, historia4
    ])

    session.commit()

    print("Datos ingresados correctamente.")

except Exception as error:
    session.rollback()
    print("Error al ingresar los datos:", error)

finally:
    session.close()
