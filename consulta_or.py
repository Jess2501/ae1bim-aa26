from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import Engine, RecursoAcademico

Session = sessionmaker(bind=Engine)
session = Session()

print("\n--- 5. Uso de OR_() (Buscar recursos que sean tipo 'Video' O de la carrera de Medicina) ---")
recursos = session.query(RecursoAcademico).filter(
    or_(
        RecursoAcademico.tipo == 'Video',
        RecursoAcademico.carrera_id == 2
    )
).all()

for r in recursos:
    print(f"Recurso (OR): {r.titulo} | Tipo: {r.tipo}")

session.close()