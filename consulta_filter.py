from sqlalchemy.orm import sessionmaker
from crear_base_entidades import Engine, RecursoAcademico

Session = sessionmaker(bind=Engine)
session = Session()

print("\n--- 2. Uso de FILTER() (Buscar recursos de tipo 'Guía de estudio') ---")
recursos = session.query(RecursoAcademico).filter(RecursoAcademico.tipo == 'Guía de estudio').all()
for r in recursos:
    print(f"Recurso: {r.titulo} | URL: {r.url}")

session.close()