# POI Backend

Backend API para la Plataforma de Planeamiento y Presupuesto.

## Requisitos

- Python 3.11+
- PostgreSQL 15+

## Instalación

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales

# Crear base de datos en PostgreSQL
# CREATE DATABASE poi_db;
# CREATE USER poi_user WITH PASSWORD 'poi_pass';
# GRANT ALL PRIVILEGES ON DATABASE opp_db TO poi_user;

# Ejecutar servidor
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000