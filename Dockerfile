#Imagen default
FROM python:3.11-slim

#Directorio de la app
WORKDIR /app

#Copiar app
COPY . /app

#dependencias (requirements)
RUN pip install --no-cache-dir -r requirements.txt

#Puerto default
EXPOSE 5000

#Ejecutar programa
CMD ["python", "run.py"]