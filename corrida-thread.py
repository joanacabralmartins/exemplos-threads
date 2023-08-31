import random
import time
import threading

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

def iniciar_corrida(num_threads):
    threads = []
    resultados = []

    def thread_secundaria(id_da_thread):
        total_passos = realizar_corrida(id_da_thread)
        resultados.append(total_passos)

    for i in range(num_threads):
        thread = threading.Thread(target=thread_secundaria, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    indice_vencedor = resultados.index(min(resultados))
    id_da_thread_vencedora = indice_vencedor + 1
    print(f'Thread {id_da_thread_vencedora} venceu com {resultados[indice_vencedor]} passos')

if __name__ == "__main__":
    num_threads = 2
    iniciar_corrida(num_threads)