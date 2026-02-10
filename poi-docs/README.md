# POI Platform - Plataforma de Planeamiento y Presupuesto

Plataforma web multi-tenant para gestión de planeamiento y presupuesto en entidades públicas.

## Estructura

- `poi-backend/` - Backend API (FastAPI + PostgreSQL)
- `poi-frontend/` - Frontend (React + TypeScript)
- `poi-shared/` - Tipos compartidos

## Inicio rápido (Backend)

```bash
cd opp-backend

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales

# Ejecutar servidor
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000