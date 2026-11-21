
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Engine, Veterinario

Session = sessionmaker(bind=Engine)
session = Session()

# Ordenar veterinarios por apellido
resultados = (
    session.query(Veterinario)
    .order_by(Veterinario.apellidos.asc())
    .all()
)

print("\nVETERINARIOS ORDENADOS POR APELLIDO")

for veterinario in resultados:
    print(
        veterinario.apellidos,
        veterinario.nombres,
        "- Licencia:",
        veterinario.licencia
    )

session.close()
