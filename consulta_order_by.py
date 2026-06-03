from sqlalchemy.orm import sessionmaker
from crear_base_entidades import Engine, Facultad

Session = sessionmaker(bind=Engine)
session = Session()

print("\n--- 3. Uso de ORDER_BY() (Listar facultades ordenadas por nombre de forma descendente) ---")
facultades = session.query(Facultad).order_by(Facultad.nombre.desc()).all()
for f in facultades:
    print(f"Facultad: {f.nombre} | Decano: {f.decano}")

session.close()