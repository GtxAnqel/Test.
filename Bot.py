import json
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import time

init(autoreset=True)

BILGI_DOSYA = "ogrenilen_bilgiler.json"

# Temel sorular ve cevaplar
temel_bilgiler = {
    "merhaba": "Merhaba dostum! Sana nasıl yardımcı olabilirim?",
    "nasılsın": "İyiyim, teşekkür ederim. Sen nasılsın?",
    "ben kimim": "Sen benim sadık dostumsun, Demir.",
    "sen kimsin": "Ben kodlama ve sohbet dostunum, her zaman yanındayım.",
}

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
    url = f"https://www.google.com/search?q={soru.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        for g in soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd'):
            if g.text:
                return g.text
    except Exception:
        return "Web aramasında bir hata oluştu."
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
        soru = input(Fore.BLUE + "Sen: ").lower().strip()
        if soru == "çık":
            print(Fore.RED + "Görüşürüz dostum, kendine iyi bak!")
            break

        # Öncelikle temel bilgiler kontrolü
        if soru in temel_bilgiler:
            print(Fore.GREEN + "Bot:", temel_bilgiler[soru])
            continue

        # Öğrenilmiş cevap varsa ver
        if soru in bilgiler:
            print(Fore.GREEN + "Bot:", bilgiler[soru])
            continue

        # Öğrenme modu: "öğren" komutu
        if soru == "öğren":
            yeni_soru = input(Fore.BLUE + "Öğrenmemi istediğin soru nedir? ").lower().strip()
            yeni_cevap = input(Fore.BLUE + f"'{yeni_soru}' sorusunun cevabı nedir? ").strip()
            bilgiler[yeni_soru] = yeni_cevap
            bilgi_kaydet(bilgiler)
            print(Fore.GREEN + f"Tamam dostum, '{yeni_soru}' bilgisini öğrendim.")
            continue

        # Öğret komutu: "öğret echo Yazıyı ekrana yazdırır"
        if soru.startswith("öğret "):
            try:
                _, key, *cevap_parcasi = soru.split()
                cevap = " ".join(cevap_parcasi)
                bilgiler[key] = cevap
                bilgi_kaydet(bilgiler)
                print(Fore.GREEN + f"Tamam dostum, '{key}' bilgisini öğrendim.")
            except Exception:
                print(Fore.RED + "Öğretme formatı yanlış, şöyle dene: öğret echo Yazıyı ekrana yazdırır")
            continue

        # Özel komut GTX (şimdilik boş)
        if soru.startswith("gtx sana emrediyor"):
            print(Fore.GREEN + "Tamam dostum, komutları belleğe yüklüyorum...")
            # Gelişmiş fonksiyonlar buraya eklenebilir
            continue

        # Web araması komutu: "web <soru>"
        if soru.startswith("web "):
            arama_sorusu = soru[4:].strip()
            cevap = webden_ara(arama_sorusu)
            print(Fore.GREEN + "Bot (Webden):", cevap)
            continue

        # Bilinmeyen sorularda öğrenme önerisi
        print(Fore.GREEN + "Bot: Bu soruyu bilmiyorum dostum. Öğrenmemi ister misin? (evet/hayır)")
        cevap = input(Fore.BLUE + "Sen: ").lower().strip()
        if cevap == "evet":
            yeni_cevap = input(Fore.BLUE + f"'{soru}' sorusunun cevabını yaz: ").strip()
            bilgiler[soru] = yeni_cevap
            bilgi_kaydet(bilgiler)
            print(Fore.GREEN + "Tamam dostum, öğrendim.")
        else:
            print(Fore.GREEN + "Peki dostum, başka bir şey sorabilirsin.")

        time.sleep(0.3)

if __name__ == "__main__":
    main()
