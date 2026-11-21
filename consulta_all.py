
from sqlalchemy import func
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

# Consultar clínicas y contar sus historias clínicas
resultados = (
    session.query(
        Clinica.nombre,
        func.count(HistoriaClinica.id).label("total_historias")
    )
    .outerjoin(Clinica.consultorios)
    .outerjoin(Consultorio.veterinarios)
    .outerjoin(Veterinario.historias)
    .group_by(Clinica.id, Clinica.nombre)
    .all()
)

print("\nCLINICAS Y NUMERO DE HISTORIAS CLINICAS")

for nombre, total in resultados:
    print("Clinica:", nombre)
    print("Historias clinicas:", total)
    print("-----------------------------")

session.close()
