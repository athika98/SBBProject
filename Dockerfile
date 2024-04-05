# Usage
# docker build -t pasupath/sbbprojects .
# docker run --name sbbprojects -e AZURE_STORAGE_CONNECTION_STRING='***' -p 9001:5000 -d pasupath/sbbprojects
FROM python:3.12.1 AS backend

# Copy Files
WORKDIR /usr/src/app/backend
#COPY backend/backend.py backend/backend.py
#COPY frontend/build frontend/build
COPY backend/ .

# Install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM node:20 AS frontend

# Setze das Arbeitsverzeichnis im Container
WORKDIR /usr/src/app/frontend

# Kopiere das Frontend-Verzeichnis in den Container
COPY frontend/ .

# Installiere Node-Abhängigkeiten und baue das Frontend
RUN npm install && npm run build

# Kopiere das gebaute Frontend in das Backend-Verzeichnis
FROM backend
COPY --from=frontend /usr/src/app/frontend/build /usr/src/app/frontend/build

# Docker Run Command
EXPOSE 5000
ENV FLASK_APP=/usr/src/app/backend/backend.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]