from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import Engine, Profesor

Session = sessionmaker(bind=Engine)
session = Session()

print("\n--- 4. Uso de AND_() (Profesor con especialidad Desarrollo Web Y de la carrera de Software) ---")
profesores = session.query(Profesor).filter(
    and_(
        Profesor.especialidad == 'Desarrollo Web',
        Profesor.carrera_id == 1
    )
).all()

for p in profesores:
    print(f"Profesor encontrado (AND): {p.nombre} | Correo: {p.correo}")

session.close()