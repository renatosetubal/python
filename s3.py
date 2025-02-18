import boto3
import os
from dotenv import load_dotenv

load_dotenv()
SOURCE_ENDPOINT=os.getenv("SOURCE_ENDPOINT")
SOURCE_ACCESS_KEY =os.getenv("SOURCE_ACCESS_KEY")
SOURCE_SECRET_KEY = os.getenv("SOURCE_SECRET_KEY")
LOCAL_SYNC_DIR = "./synced_data"

def create_s3_client(endpoint, access_key, secret_key):
    return boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        verify=True  
    )

def list_buckets(s3_client):
    try:
        # Chama o método list_buckets() para obter a lista de buckets
        response = s3_client.list_buckets()
        
        # Extrai os nomes dos buckets da resposta
        buckets = [bucket["Name"] for bucket in response.get("Buckets", [])]
        
        # Exibe os buckets encontrados (opcional, para fins de depuração)
        if buckets:
            print("Buckets disponíveis:")
            for bucket in buckets:
                print(f"- {bucket}")
        else:
            print("Nenhum bucket encontrado.")
        
        # Retorna a lista de buckets
        return buckets

    except Exception as e:
        print(f"Erro ao listar buckets: {e}")
        return []  # Retorna uma lista vazia em caso de erro

def sync_bucket_to_local(s3_client, bucket, local_dir):
    """Sincroniza todos os objetos de um bucket para um diretório local."""
    print(f"Sincronizando objetos do bucket '{bucket}' para o diretório local '{local_dir}'...")
    # Cria o diretório local se ele não existir
    os.makedirs(local_dir, exist_ok=True)
    # Lista todos os objetos no bucket de origem
    try:
        paginator = s3_client.get_paginator("list_objects_v2")
        page_iterator = paginator.paginate(Bucket=bucket)
        for page in page_iterator:
            if "Contents" not in page:
                print(f"Nenhum objeto encontrado no bucket '{bucket}'.")
                continue
            for obj in page["Contents"]:
                key = obj["Key"]
                local_path = os.path.join(local_dir, bucket, key)  # Inclui o nome do bucket no caminho local
                # Cria subdiretórios, se necessário
                os.makedirs(os.path.dirname(local_path), exist_ok=True)
                # Baixa o objeto para o diretório local
                print(f"Baixando objeto: {key} -> {local_path}")
                s3_client.download_file(bucket, key, local_path)
        print(f"Sincronização concluída para o bucket '{bucket}'.\n")
    except Exception as e:
        print(f"Erro ao sincronizar o bucket '{bucket}': {e}")
   
source_client = create_s3_client(SOURCE_ENDPOINT, SOURCE_ACCESS_KEY, SOURCE_SECRET_KEY)
source_buckets = list_buckets(source_client)
for bucket in source_buckets:
    bucket_local_dir = os.path.join(LOCAL_SYNC_DIR, bucket)  # Cada bucket tem seu próprio subdiretório
    sync_bucket_to_local(source_client, bucket, bucket_local_dir)