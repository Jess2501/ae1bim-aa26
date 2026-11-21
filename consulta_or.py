
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import (
    Engine,
    Veterinario,
    Consultorio
)

Session = sessionmaker(bind=Engine)
session = Session()

# Buscar veterinarios de Medicina General o Cirugía
resultados = (
    session.query(Veterinario)
    .join(Veterinario.consultorio)
    .filter(
        or_(
            Consultorio.especialidad == "Medicina General",
            Consultorio.especialidad == "Cirugia"
        )
    )
    .all()
)

print("\nVETERINARIOS DE MEDICINA GENERAL O CIRUGIA")

for veterinario in resultados:
    print("Nombre:", veterinario.nombres, veterinario.apellidos)
    print("Especialidad:", veterinario.consultorio.especialidad)
    print("-----------------------------")

session.close()
