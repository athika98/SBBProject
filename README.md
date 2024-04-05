# SBB Project

inspired by https://github.com/mosazhaw/HikePlanner

## Backend
* Scrape SBB data via API 
* BFS Data csv
* Load data into MongoDB
* Update model
* Save model to backend/modelGA.pkl and backend/modelHA.pkl

## Azure Blob Storage

* Save model to Azure Blob Storage
* Always save new version of model
* Zugriff: Speicherkonto > Zugriffsschlüssel
    * Als Umgebungsvariable für Docker
    * Als Secret für GitHub

## GitHub Action
* Scrape
* Load data to MongoDB (Azure Cosmos DB)
* Update model and save to Azure Blob Storage

## App
* Backend: Python Flask (backend/backend.py)
* Frontend: SvelteKit (build still manually)

## Deployment with Docker

* Dockerfile
* Install dependencies with pip
* Copy Frontend (prebuilt, TODO Build)
* Azure Blob Storage: Zugriffsschlüssel als Umgebungsvariable

