#### Imports ####
import os, uuid, argparse
from azure.storage.blob import BlobServiceClient
#### Imports ####

# ArgumentParser zum Erfassen der Befehlszeilenargumente
parser = argparse.ArgumentParser(description='Upload Models to Azure Blob Storage')
parser.add_argument('-c', '--connection', required=True, help="Azure storage connection string")
parser.add_argument('-f', '--files', nargs='+', required=True, help="Files to upload")
args = parser.parse_args()

try:
    print("Azure Blob Storage v2 quickstart sample")

    # Erstelle das BlobServiceClient-Objekt
    blob_service_client = BlobServiceClient.from_connection_string(args.connection)

    # Liste vorhandene Container und bestimme die nächste Nummer für den neuen Container
    containers = blob_service_client.list_containers(include_metadata=True)
    suffix = 0
    for container in containers:
        if container['name'].startswith("sbbproject-model"):
            parts = container['name'].split("-")
            if len(parts) > 1 and parts[-1].isdigit():
                suffix = max(suffix, int(parts[-1]))
    suffix += 1  # Inkrementiere die Nummer für den neuen Container
    container_name = f"sbbproject-model-{suffix}"
    print(f"Creating new container: {container_name}")
    container_client = blob_service_client.create_container(container_name)

    # Lade jede angegebene Datei hoch
    for local_file_name in args.files:
        # Pfad zum Ordner 'project', der eine Ebene über 'data_and_backend' liegt
        project_folder_path = os.path.join("..", "..", "SBBProject-20240329")
        upload_file_path = os.path.join(project_folder_path, local_file_name)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
        print(f"\nUploading to Azure Storage as blob:\n\t{local_file_name}")
        with open(upload_file_path, mode="rb") as data:
            blob_client.upload_blob(data)

except Exception as ex:
    print('Exception occurred:')
    print(ex)
