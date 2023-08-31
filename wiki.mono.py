import requests

async def get_wiki_page_existence(wiki_page_url):
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