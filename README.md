
# Sistema de Gestión de Clínicas Veterinarias

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de gestión para una red de clínicas veterinarias, utilizando Python, SQLite y la librería SQLAlchemy mediante el concepto de ORM.

El sistema permite administrar clínicas, consultorios, veterinarios e historias clínicas, estableciendo relaciones entre las diferentes entidades.

## Tecnologías utilizadas

- Python
- SQLite
- SQLAlchemy (ORM)

## Entidades del sistema

1. **Clínica:** almacena el nombre comercial, dirección y médico veterinario responsable.
2. **Consultorio:** registra el nombre, número y especialidad, y pertenece a una clínica.
3. **Veterinario:** almacena nombres, apellidos, correo electrónico y licencia profesional.
4. **Historia Clínica:** registra fecha de atención, diagnóstico, tratamiento y nombre de la mascota.

## Relaciones entre entidades

- Una clínica puede tener varios consultorios.
- Un consultorio pertenece a una clínica y puede tener varios veterinarios.
- Un veterinario pertenece a un consultorio y puede elaborar varias historias clínicas.
- Cada historia clínica pertenece a un veterinario.

## Consultas ORM implementadas

Se desarrollaron las siguientes consultas utilizando SQLAlchemy:

- **all():** muestra todas las clínicas y el número de historias clínicas asociadas a cada una.
- **filter():** filtra veterinarios según su especialidad.
- **order_by():** ordena los veterinarios alfabéticamente por sus apellidos.
- **or():** busca veterinarios de Medicina General o Cirugía.
- **and():** busca historias clínicas que cumplen dos condiciones simultáneamente.

## Archivos del proyecto

- `configuracion.py`
- `crear_base_entidades.py`
- `poblar_base.py`
- `consulta_all.py`
- `consulta_filter.py`
- `consulta_order_by.py`
- `consulta_or.py`
- `consulta_and.py`
- `clinicas_veterinarias.db`

## Ejecución del proyecto

Primero instalar SQLAlchemy:

```bash
python -m pip install sqlalchemy
```

Después ejecutar los archivos en este orden:

1. `python crear_base_entidades.py`
2. `python poblar_base.py`
3. `python consulta_all.py`
4. `python consulta_filter.py`
5. `python consulta_order_by.py`
6. `python consulta_or.py`
7. `python consulta_and.py`

## Autor

Proyecto académico desarrollado como actividad práctica de ORM con SQLAlchemy.
