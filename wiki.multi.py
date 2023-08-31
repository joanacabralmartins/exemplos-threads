import requests
import threading
import time

def get_wiki_page_existence(wiki_page_url):
    try:
        response = requests.get(wiki_page_url)
        page_status = "unknown"

        if response.status_code == 200:
            page_status = "Existe"
        elif response.status_code == 404:
            page_status = "Não existe"

        return f"{wiki_page_url} - {page_status}"
    except Exception as error:
        return f"{wiki_page_url} - error: {str(error)}"

def worker_function(chunk, results):
    results.extend([get_wiki_page_existence(url) for url in chunk])

def main():
    print("Executando com Threads:")

    NUM_WORKERS = 4
    wiki_page_urls = [f"https://en.wikipedia.org/wiki/{i + 1}" for i in range(50)]

    chunk_size = len(wiki_page_urls) // NUM_WORKERS
    chunks = [wiki_page_urls[i:i + chunk_size] for i in range(0, len(wiki_page_urls), chunk_size)]

    results = []
    threads = []

    start_time = time.time()

    for chunk in chunks:
        thread = threading.Thread(target=worker_function, args=(chunk, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    for result in results:
        print(result)

    elapsed_time = end_time - start_time
    print(f"Tempo total de execução: {elapsed_time:.2f} segundos")

if __name__ == "__main__":
    main()
