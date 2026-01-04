import requests
from bs4 import BeautifulSoup

def get_trending_repos():
    url = "https://github.com/trending"
    headers = {"User-Agent": "Mozilla/5.0"} # Ez jelzi a szervernek, hogy nem bot vagyunk
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "Hiba az oldal elérésekor"

    soup = BeautifulSoup(response.text, 'html.parser')
    repos = soup.find_all('h2', class_='h3 lh-condensed', limit=5)

    trending_list = []
    for repo in repos:
        name = repo.get_text(strip=True).replace(' ', '')
        trending_list.append(name)
    
    return trending_list

def update_readme(trending_list):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = ""
    end_marker = ""
    
    if start_marker not in content or end_marker not in content:
        return # Ha nincs ott a jelölő, nem csinál semmit

    new_text = f"{start_marker}\n" + "\n".join([f"- {repo}" for repo in trending_list]) + f"\n{end_marker}"
    
    # Kicseréljük a régi részt az új listával
    import re
    pattern = f"{start_marker}.*?{end_marker}"
    updated_content = re.sub(pattern, new_text, content, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    trending = get_trending_repos()
    if isinstance(trending, list):
        update_readme(trending)
        print("Siker! A README.md frissítve a trending projektekkel.")
