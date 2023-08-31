import random
import time

def gerar_numeros_aleatorios():
    return random.randint(1, 5)

def esperar(segundos):
    time.sleep(segundos)

def realizar_corrida(id_da_thread):
    posicao_atual = 0
    total_passos = 0

    print(f'Thread {id_da_thread} - Iniciando')

    while posicao_atual < 50:
        passos = gerar_numeros_aleatorios()
        total_passos += passos
        posicao_atual += passos

        print(f'Vez da thread {id_da_thread}')
        print(f'Numero sorteado: {passos}')
        print(f'Thread {id_da_thread} Andou {passos} casas')
        print(f'Posição atual da thread {id_da_thread}: {posicao_atual}')

        esperar(1)

    print(f'Thread {id_da_thread} - Chegou à posição 50! Total de passos: {total_passos}')
    return total_passos