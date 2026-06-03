from sqlalchemy.orm import sessionmaker
from crear_base_entidades import Engine, Facultad, Carrera, Profesor, RecursoAcademico

Session = sessionmaker(bind=Engine)
session = Session()

try:
    # 1. Crear Facultad
    fac1 = Facultad(nombre='Facultad de Ingeniería y Ciencias', ubicacion='Campus Central - Bloque A', decano='Dr. Carlos Mendoza')
    fac2 = Facultad(nombre='Facultad de Ciencias de la Salud', ubicacion='Campus Norte - Edificio Médico', decano='Dra. María Espinoza')
    
    # 2. Crear Carreras
    car1 = Carrera(nombre='Software', codigo='SOFT-001', facultad=fac1)
    car2 = Carrera(nombre='Medicina', codigo='MED-002', facultad=fac2)
    
    # 3. Crear Profesores
    prof1 = Profesor(nombre='Alex Valdiviezo', especialidad='Desarrollo Web', correo='avaldiviezo@universidad.edu.ec', carrera=car1)
    prof2 = Profesor(nombre='Dr. Luis Segura', especialidad='Anatomía', correo='lsegura@universidad.edu.ec', carrera=car2)
    
    # 4. Crear Recursos Académicos
    rec1 = RecursoAcademico(titulo='Guía de Estudio: Introducción a SQLAlchemy', tipo='Guía de estudio', url='https://recursos.univ.edu.ec/software/sqlalchemy-intro', carrera=car1)
    rec2 = RecursoAcademico(titulo='Video: Simulación del Sistema Circulatorio', tipo='Video', url='https://recursos.univ.edu.ec/medicina/circulatorio', carrera=car2)
    
    # Agregar y guardar todo
    session.add_all([fac1, fac2, prof1, prof2, rec1, rec2])
    session.commit()
    print("Datos demográficos y académicos insertados correctamente.")
    
except Exception as e:
    session.rollback()
    print(f"Error al poblar la base de datos: {e}")
finally:
    session.close()