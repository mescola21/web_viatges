FROM python:3.13-slim

WORKDIR /app

# Instala Poetry
RUN pip install poetry

# Copia los archivos de configuración de Poetry
COPY pyproject.toml poetry.lock ./

# Copia el código fuente


# Configura Poetry para no crear virtualenv y luego instala las dependencias
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY . .

# Expone el puerto 8000 de Django
EXPOSE 8000

# Cambia CMD para usar python directamente
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
