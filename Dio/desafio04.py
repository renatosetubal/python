N = int(input())

# Iterar sobre os casos de teste
for _ in range(N):
    A, B = input().split()

    # Verificar se A e B têm até 1000 dígitos
    if len(A) > 1000 or len(B) > 1000:
        print("Valores devem ter no máximo 1000 dígitos.")
        continue

    # Verificar se B corresponde aos últimos dígitos de A
    if A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")