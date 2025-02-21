import hashlib

#1-Verificar os algorítmos disponíveis para uso
print(hashlib.algorithms_available)

#2 -Verificar algoritmos de acordo com o sistema operacional
print(hashlib.algorithms_guaranteed)

#3 - Utilizando sha256
algo=hashlib.sha3_256()
print(algo.digest())
message="Esta é uma frase criptografada em sha256".encode()
algo.update(message)
print(algo.hexdigest())


#4- Utilizando MD5
md5=hashlib.md5()
md5.update(message)
print(md5.hexdigest())