
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Engine, HistoriaClinica

Session = sessionmaker(bind=Engine)
session = Session()

# Buscar historias clínicas que cumplan ambas condiciones
resultados = (
    session.query(HistoriaClinica)
    .filter(
        and_(
            HistoriaClinica.diagnostico == "Gastroenteritis",
            HistoriaClinica.tratamiento == "Medicamentos y dieta especial"
        )
    )
    .all()
)

print("\nHISTORIAS CLINICAS CON AMBAS CONDICIONES")

for historia in resultados:
    print("Mascota:", historia.mascota)
    print("Diagnostico:", historia.diagnostico)
    print("Tratamiento:", historia.tratamiento)
    print("-----------------------------")

session.close()
