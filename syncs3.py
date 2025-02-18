import boto3
import os

# Configurações do servidor MinIO de origem
SOURCE_ENDPOINT = "https://minio-origem.example.com"  # Endpoint do MinIO de origem
SOURCE_ACCESS_KEY = "your-source-access-key"
SOURCE_SECRET_KEY = "your-source-secret-key"
SOURCE_BUCKET = "source-bucket-name"

# Configurações do servidor MinIO de destino
DEST_ENDPOINT = "https://minio-destino.example.com"  # Endpoint do MinIO de destino
DEST_ACCESS_KEY = "your-dest-access-key"
DEST_SECRET_KEY = "your-dest-secret-key"
DEST_BUCKET = "destination-bucket-name"

# Diretório local para sincronização (opcional)
LOCAL_SYNC_DIR = "./synced_data"  # Diretório local para salvar os arquivos


def create_s3_client(endpoint, access_key, secret_key):
    """Cria um cliente S3 configurado para o endpoint fornecido."""
    return boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        verify=False  # Desativa a verificação SSL (use apenas em ambientes confiáveis)
    )


def sync_buckets(source_client, dest_client, source_bucket, dest_bucket):
    """Sincroniza objetos de um bucket de origem para um bucket de destino."""
    print(f"Sincronizando objetos de '{source_bucket}' para '{dest_bucket}'...")
    
    # Lista todos os objetos no bucket de origem
    response = source_client.list_objects_v2(Bucket=source_bucket)
    if "Contents" not in response:
        print("Nenhum objeto encontrado no bucket de origem.")
        return

    for obj in response["Contents"]:
        key = obj["Key"]
        print(f"Processando objeto: {key}")

        # Verifica se o objeto já existe no bucket de destino
        try:
            dest_client.head_object(Bucket=dest_bucket, Key=key)
            print(f"Objeto '{key}' já existe no bucket de destino. Pulando...")
        except dest_client.exceptions.ClientError:
            # Se o objeto não existir no destino, copia-o
            print(f"Copiando objeto '{key}' para o bucket de destino...")
            copy_source = {"Bucket": source_bucket, "Key": key}
            dest_client.copy_object(CopySource=copy_source, Bucket=dest_bucket, Key=key)

    print("Sincronização concluída!")


def sync_to_local(source_client, source_bucket, local_dir):
    """Sincroniza objetos de um bucket de origem para um diretório local."""
    print(f"Sincronizando objetos de '{source_bucket}' para o diretório local '{local_dir}'...")
    
    # Cria o diretório local se ele não existir
    os.makedirs(local_dir, exist_ok=True)

    # Lista todos os objetos no bucket de origem
    response = source_client.list_objects_v2(Bucket=source_bucket)
    if "Contents" not in response:
        print("Nenhum objeto encontrado no bucket de origem.")
        return

    for obj in response["Contents"]:
        key = obj["Key"]
        local_path = os.path.join(local_dir, key)

        # Cria subdiretórios, se necessário
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        # Baixa o objeto para o diretório local
        print(f"Baixando objeto: {key} -> {local_path}")
        source_client.download_file(source_bucket, key, local_path)

    print("Sincronização concluída!")


if __name__ == "__main__":
    # Cria clientes S3 para origem e destino
    source_client = create_s3_client(SOURCE_ENDPOINT, SOURCE_ACCESS_KEY, SOURCE_SECRET_KEY)
    dest_client = create_s3_client(DEST_ENDPOINT, DEST_ACCESS_KEY, DEST_SECRET_KEY)

    # Escolha o tipo de sincronização desejada
    sync_buckets(source_client, dest_client, SOURCE_BUCKET, DEST_BUCKET)
    # Ou sincronize para um diretório local
    # sync_to_local(source_client, SOURCE_BUCKET, LOCAL_SYNC_DIR)