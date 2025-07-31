
import json
from colorama import Fore, Style, init

init(autoreset=True)

SIFRE = "7202411417512"

# JSON dosyalarından komutları ve araçları yükle
def json_oku(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(Fore.RED + f"{dosya_adi} bulunamadı, boş sözlük olarak başlatılıyor.")
        return {}
    except json.JSONDecodeError:
        print(Fore.RED + f"{dosya_adi} dosyası okunurken hata oluştu, boş sözlük olarak başlatılıyor.")
        return {}

# JSON dosyasına veri kaydet
def json_kaydet(dosya_adi, veri):
    try:
        with open(dosya_adi, "w", encoding="utf-8") as f:
            json.dump(veri, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(Fore.RED + f"{dosya_adi} dosyasına kaydederken hata: {e}")

python_komutlari = json_oku("py_kodları.json")
python_araclari = json_oku("py_araçları.json")

def sifre_kontrol():
    for hak in range(3):
        girilen = input(Fore.YELLOW + "Lütfen şifreni gir: ")
        if girilen == SIFRE:
            print(Fore.GREEN + "Giriş başarılı! Hoş geldin.")
            return True
        else:
            print(Fore.RED + f"Hatalı şifre! {2 - hak} hakkınız kaldı.")
    print(Fore.RED + "Çok fazla hatalı giriş. Bot kapanıyor.")
    return False

def illegal_sifre_kontrol():
    for hak in range(3):
        girilen = input(Fore.YELLOW + "Bu araç için şifre gerekli. Lütfen şifrenizi girin: ")
        if girilen == SIFRE:
            print(Fore.GREEN + "Şifre doğru, erişim verildi.")
            return True
        else:
            print(Fore.RED + f"Hatalı şifre! {2 - hak} hakkınız kaldı.")
    print(Fore.RED + "Şifre doğrulanamadı, erişim engellendi.")
    return False

def kod_bilgisi_ver(kelime):
    kelime = kelime.lower()
    if kelime in python_komutlari:
        k = python_komutlari[kelime]
        return f"{Style.BRIGHT}Python Komutu: {kelime}\nAçıklama: {k['aciklama']}\nÖrnek:\n{k['ornek']}"
    elif kelime in python_araclari:
        a = python_araclari[kelime]
        # Illegal ise şifre sor
        if a.get("illegal", False):
            if not illegal_sifre_kontrol():
                return "Bu araca erişim için şifre doğrulanamadı."
        return f"{Style.BRIGHT}Araç: {kelime}\nAçıklama: {a['aciklama']}\nÖrnek Kod:\n{a['ornek']}"
    else:
        return "Üzgünüm dostum, bunu bilmiyorum."

def yorumla_ve_uret(metin):
    metin = metin.lower()

    # Basit yorumlama örnekleri
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
                        json_kaydet("py_kodları.json", python_komutlari)
                        print(Fore.GREEN + f"'{komut}' Python komutu olarak eklendi.")
                    elif kategori in ("araç", "arac"):
                        python_araclari[komut] = {"aciklama": aciklama, "ornek": ornek}
                        json_kaydet("py_araçları.json", python_araclari)
                        print(Fore.GREEN + f"'{komut}' araç olarak eklendi.")
                    else:
                        print(Fore.RED + "Geçersiz kategori. python veya araç kullan.")
                else:
                    print(Fore.RED + "Açıklama ve örnek '||' ile ayrılmalı.")
            except Exception:
                print(Fore.RED + "Öğretme formatı hatalı. Örnek:\nöğret python input Kullanıcıdan veri almak için kullanılır. || isim = input('Adın ne? ')")
            continue

        cevap = yorumla_ve_uret(soru)
        print(Fore.GREEN + "Bot:\n" + cevap)


if __name__ == "__main__":
    main()
