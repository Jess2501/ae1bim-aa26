from sqlalchemy.orm import sessionmaker
from crear_base_entidades import Engine, Carrera

Session = sessionmaker(bind=Engine)
session = Session()

print("\n--- 1. Uso de ALL() (Listar todas las carreras) ---")
carreras = session.query(Carrera).all()
for c in carreras:
    print(f"Carrera: {c.nombre} | Código: {c.codigo}")

session.close()