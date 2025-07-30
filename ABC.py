import requests

url = "https://www.anime-planet.com/"

try:
    response = requests.get(url)
    if response.status_code == 200:
        # Sayfa başlığını çekelim
        start = response.text.find("<title>") + len("<title>")
        end = response.text.find("</title>")
        title = response.text[start:end]
        print(f"Site Başlığı: {title}")
    else:
        print(f"Siteye bağlanamadı, durum kodu: {response.status_code}")
except Exception as e:
    print(f"Hata oluştu: {e}")
