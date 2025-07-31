import json
from colorama import Fore, Style, init

init(autoreset=True)

# Şifre kontrolü için basit yapı (istersen çıkarabilirsin)
SIFRE = "1234"

# Python komutları + açıklama + örnek + kategori
python_komutlari = {
    "input": {
        "aciklama": "Kullanıcıdan veri almak için kullanılır.",
        "ornek": 'isim = input("Adın ne? ")',
        "kategori": "girdi"
    },
    "if": {
        "aciklama": "Koşul belirtmek için kullanılır.",
        "ornek": "if x > 5:\n    print('x 5\'ten büyük')",
        "kategori": "kontrol yapısı"
    },
    # ... burada 1000+ python komutu ve yapısı olacak
}

# Araçlar: araç ismi -> açıklama ve örnek kod
python_araclari = {
    "ip_tracer": {
        "aciklama": "Verilen IP adresini izler, konum ve servis sağlayıcı bilgisi verir.",
        "ornek": """
import requests

def ip_tracer(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    if data['status'] == 'success':
        print(f"IP: {ip}")
        print(f"Ülke: {data['country']}")
        print(f"Şehir: {data['city']}")
        print(f"ISP: {data['isp']}")
    else:
        print("IP bilgisi bulunamadı.")

ip_tracer("8.8.8.8")
"""
    },
    # ... burada +100 araç örneği olacak
}

def sifre_kontrol():
    for hak in range(3):
        girilen = input(Fore.YELLOW + "Lütfen şifreni gir: ")
        if girilen == SIFRE:
            print(Fore.GREEN + "Giriş başarılı! Hoş geldin.")
            return True
        else:
            print(Fore.RED + f"Hatalı şifre! {2-hak} hakkınız kaldı.")
    print(Fore.RED + "Çok fazla hatalı giriş. Bot kapanıyor.")
    return False

def kod_bilgisi_ver(kelime):
    """Python komutlarını veya araçlarını açıklayıp örnek verir."""
    kelime = kelime.lower()
    if kelime in python_komutlari:
        k = python_komutlari[kelime]
        return f"{Style.BRIGHT}Python Komutu: {kelime}\nAçıklama: {k['aciklama']}\nÖrnek:\n{k['ornek']}"
    elif kelime in python_araclari:
        a = python_araclari[kelime]
        return f"{Style.BRIGHT}Araç: {kelime}\nAçıklama: {a['aciklama']}\nÖrnek Kod:\n{a['ornek']}"
    else:
        return "Üzgünüm dostum, bunu bilmiyorum."

def yorumla_ve_uret(metin):
    metin = metin.lower()

    # Basit yorumlama
    if "ip tracer" in metin or "ip takip" in metin:
        return kod_bilgisi_ver("ip_tracer")
    if "input" in metin or "girdi" in metin:
        return kod_bilgisi_ver("input")
    if "if" in metin or "koşul" in metin:
        return kod_bilgisi_ver("if")
    if "menü" in metin or "menu" in metin:
        return (
            "Basit Python menü örneği:\n\n"
            "def menu():\n"
            "    while True:\n"
            "        print('1. Seçenek 1')\n"
            "        print('2. Seçenek 2')\n"
            "        print('3. Çıkış')\n"
            "        secim = input('Seçiminiz: ')\n"
            "        if secim == '3':\n"
            "            print('Çıkılıyor...')\n"
            "            break\n"
            "        else:\n"
            "            print(f'Seçilen: {secim}')\n\n"
            "menu()"
        )
    # Daha fazla yorumlama eklenebilir

    return "Dostum bunu tam anlayamadım, biraz daha açık yazabilir misin?"

def main():
    print(Fore.CYAN + Style.BRIGHT + "🤖 Gelişmiş Python Kod Botu'na Hoş Geldin! (Çıkmak için 'çık' yaz.)\n")

    if not sifre_kontrol():
        return

    while True:
        soru = input(Fore.BLUE + "Sen: ").strip().lower()
        if soru == "çık":
            print(Fore.RED + "Görüşürüz dostum, kendine iyi bak!")
            break

        # "öğret python input Kullanıcıdan veri almak için kullanılır. || isim = input('Adın ne? ')"
        if soru.startswith("öğret "):
            try:
                parcalar = soru.split()
                kategori = parcalar[1]
                komut = parcalar[2]
                aciklama_ornek = " ".join(parcalar[3:])
                if "||" in aciklama_ornek:
                    aciklama, ornek = aciklama_ornek.split("||", 1)
                    aciklama = aciklama.strip()
                    ornek = ornek.strip()
                    if kategori == "python":
                        python_komutlari[komut] = {"aciklama": aciklama, "ornek": ornek, "kategori": "öğretilen"}
                        print(Fore.GREEN + f"'{komut}' Python komutu olarak eklendi.")
                    elif kategori == "araç" or kategori == "arac":
                        python_araclari[komut] = {"aciklama": aciklama, "ornek": ornek}
                        print(Fore.GREEN + f"'{komut}' araç olarak eklendi.")
                    else:
                        print(Fore.RED + "Geçersiz kategori. python veya araç kullan.")
                else:
                    print(Fore.RED + "Açıklama ve örnek '||' ile ayrılmalı.")
            except Exception:
                print(Fore.RED + "Öğretme formatı hatalı. Örnek:\nöğret python input Kullanıcıdan veri almak için kullanılır. || isim = input('Adın ne? ')")
            continue

        # Yorumla ve cevapla
        cevap = yorumla_ve_uret(soru)
        print(Fore.GREEN + "Bot:\n" + cevap)


if __name__ == "__main__":
    main()
