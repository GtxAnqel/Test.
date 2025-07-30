import json
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import time

init(autoreset=True)

# Öğrenilen bilgilerin saklanacağı dosya
BILGI_DOSYA = "ogrenilen_bilgiler.json"

# Dosya yoksa oluştur
if not os.path.exists(BILGI_DOSYA):
    with open(BILGI_DOSYA, "w") as f:
        json.dump({}, f)

def bilgi_yukle():
    with open(BILGI_DOSYA, "r") as f:
        return json.load(f)

def bilgi_kaydet(bilgiler):
    with open(BILGI_DOSYA, "w") as f:
        json.dump(bilgiler, f, indent=2)

def webden_ara(soru):
    print(Fore.YELLOW + "Webden arama yapılıyor, lütfen bekle...")
    url = f"https://www.google.com/search?q={soru.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        for g in soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd'):
            if g.text:
                return g.text
    except Exception:
        return "Web aramasında hata oluştu."
    return "Webde cevap bulunamadı."

def renkli_yuz():
    yuz = f"""
{Fore.CYAN}    ╔════════════╗
{Fore.CYAN}    ║  {Fore.MAGENTA}^   ^  {Fore.CYAN} ║
{Fore.CYAN}    ║  {Fore.MAGENTA}  o_o  {Fore.CYAN} ║
{Fore.CYAN}    ║  {Fore.MAGENTA}  ---  {Fore.CYAN} ║
{Fore.CYAN}    ╚════════════╝
"""
    print(yuz)

def main():
    print(Fore.GREEN + Style.BRIGHT + "🤖 Sadık Dostun Hazır! (Çıkmak için 'çık' yaz.)\n")
    renkli_yuz()

    sifre = input(Fore.BLUE + "Dostum, şifreni gir: ")
    if sifre != "++":
        print(Fore.RED + "Yanlış şifre dostum, çıkıyorum...")
        return

    print(Fore.GREEN + "Giriş başarılı! Seninleyim her daim.\n")

    bilgiler = bilgi_yukle()

    while True:
        soru = input(Fore.BLUE + "Sen: ").lower()
        if soru == "çık":
            print(Fore.RED + "Görüşürüz dostum, kendine iyi bak!")
            break

        # Öğrenilmiş cevap varsa ver
        if soru in bilgiler:
            print(Fore.GREEN + "Bot:", bilgiler[soru])
            continue

        # Öğrenme komutu örneği: "öğret echo Terminalde yazıyorsun"
        if soru.startswith("öğret "):
            try:
                _, key, *cevap_parcasi = soru.split()
                cevap = " ".join(cevap_parcasi)
                bilgiler[key] = cevap
                bilgi_kaydet(bilgiler)
                print(Fore.GREEN + f"Tamam dostum, '{key}' bilgisini öğrendim.")
            except Exception:
                print(Fore.RED + "Öğretme formatı yanlış, şöyle dene: öğret echo Terminalde yazıyorsun")
            continue

        # Özel komut: GTX ile başlayan komutları belleğe yükle (örnek)
        if soru.startswith("gtx sana emrediyor"):
            print(Fore.GREEN + "Tamam dostum, komutları belleğe yüklüyorum...")
            # Burada gelişmiş bir yükleme fonksiyonu eklenebilir
            continue

        # Öğrenilmemişse webden ara
        cevap = webden_ara(soru)
        print(Fore.GREEN + "Bot (Webden):", cevap)
        time.sleep(0.3)

if __name__ == "__main__":
    main()
