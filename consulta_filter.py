
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import (
    Engine,
    Veterinario,
    Consultorio
)

Session = sessionmaker(bind=Engine)
session = Session()

# Buscar veterinarios de Medicina General
resultados = (
    session.query(Veterinario)
    .join(Veterinario.consultorio)
    .filter(Consultorio.especialidad == "Medicina General")
    .all()
)

print("\nVETERINARIOS DE MEDICINA GENERAL")

for veterinario in resultados:
    print("Nombres:", veterinario.nombres)
    print("Apellidos:", veterinario.apellidos)
    print("Correo:", veterinario.correo)
    print("-----------------------------")

session.close()
