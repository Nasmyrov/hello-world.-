import requests

def oldal_ellenorzes(url):
    try:
        # Megpróbáljuk lekérni az oldalt 5 másodperces időkorláttal
        response = requests.get(url, timeout=5)
        return response.status_code
    except Exception:
        return None

if __name__ == "__main__":
    status = oldal_ellenorzes("https://github.com")
    print(f"GitHub állapota: {status}")
