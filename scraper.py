import requests
from bs4 import BeautifulSoup

def update_readme(trending):
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        start_marker = ""
        end_marker = ""

        start_pos = content.find(start_marker)
        end_pos = content.find(end_marker)

        if start_pos != -1 and end_pos != -1:
            new_text = "\n".join([f"- [{item.strip()}](https://github.com/{item.replace(' ', '')})" for item in trending])
            new_content = (
                content[:start_pos + len(start_marker)] +
                "\n\n" + new_text + "\n\n" +
                content[end_pos:]
            )
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(new_content)
            print("README sikeresen frissítve!")
        else:
            print("Hiba: Markerek nem találhatók!")
    except Exception as e:
        print(f"Hiba történt a fájl írásakor: {e}")

def get_trending_repos():
    url = "https://github.com/trending"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        repos = []
        for row in soup.select('article.Box-row h2 a'):
            repo_name = row.get_text(strip=True).replace(' / ', '/')
            repos.append(repo_name)
        return repos[:10]
    except Exception as e:
        print(f"Hiba a letöltéskor: {e}")
        return []

if __name__ == "__main__":
    real_data = get_trending_repos()
    if real_data:
        update_readme(real_data)
    else:
        print("Nem sikerült adatokat gyűjteni.")
