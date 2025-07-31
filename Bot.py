import json
from colorama import Fore, Style, init

# Colorama'yı otomatik sıfırlama ile başlat
init(autoreset=True)

# Sabit şifre
SIFRE = "7202411417512"

# JSON dosyalarından veri okuma fonksiyonu
def json_oku(dosya_adi):
    """Belirtilen JSON dosyasını okur ve içeriğini döndürür.
    Dosya bulunamazsa veya okunamazsa boş bir sözlük döndürür."""
    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(Fore.RED + f"{dosya_adi} bulunamadı, boş sözlük olarak başlatılıyor.")
        return {}
    except json.JSONDecodeError:
        print(Fore.RED + f"{dosya_adi} dosyası okunurken hata oluştu, boş sözlük olarak başlatılıyor.")
        return {}
    except Exception as e:
        print(Fore.RED + f"JSON okuma sırasında beklenmeyen hata ({dosya_adi}): {e}")
        return {}

# JSON dosyasına veri kaydetme fonksiyonu
def json_kaydet(dosya_adi, veri):
    """Veriyi belirtilen JSON dosyasına kaydeder."""
    try:
        with open(dosya_adi, "w", encoding="utf-8") as f:
            json.dump(veri, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(Fore.RED + f"{dosya_adi} dosyasına kaydederken hata: {e}")

# JSON dosyalarını yükle
python_komutlari = json_oku("py_kodları.json")
python_araclari = json_oku("py_araçları.json")

# Şifre kontrolü (ana giriş için)
def sifre_kontrol():
    """Botun ana girişi için şifre kontrolü yapar."""
    for hak in range(3):
        girilen = input(Fore.YELLOW + "Lütfen şifreni gir: ")
        if girilen == SIFRE:
            print(Fore.GREEN + "Giriş başarılı! Hoş geldin.")
            return True
        else:
            print(Fore.RED + f"Hatalı şifre! {2 - hak} hakkınız kaldı.")
    print(Fore.RED + "Çok fazla hatalı giriş. Bot kapanıyor.")
    return False

# Şifre kontrolü (illegal araçlar için)
def illegal_sifre_kontrol():
    """Yasa dışı olarak işaretlenmiş araçlara erişim için şifre kontrolü yapar."""
    for hak in range(3):
        girilen = input(Fore.YELLOW + "Bu araç için şifre gerekli. Lütfen şifrenizi girin: ")
        if girilen == SIFRE:
            print(Fore.GREEN + "Şifre doğru, erişim verildi.")
            return True
        else:
            print(Fore.RED + f"Hatalı şifre! {2 - hak} hakkınız kaldı.")
    print(Fore.RED + "Şifre doğrulanamadı, erişim engellendi.")
    return False

# Komut veya araç bilgisi döndürme
def kod_bilgisi_ver(kelime):
    """Verilen kelimeye göre Python komutu veya araç bilgisi döndürür."""
    kelime = kelime.lower()
    if kelime in python_komutlari:
        k = python_komutlari[kelime]
        return (f"{Style.BRIGHT}{Fore.CYAN}Python Komutu: {kelime}\n"
                f"{Fore.WHITE}Açıklama: {k.get('aciklama', 'Açıklama bulunamadı.')}\n"
                f"{Fore.LIGHTBLACK_EX}Örnek:\n{k.get('ornek', 'Örnek bulunamadı.')}")
    elif kelime in python_araclari:
        a = python_araclari[kelime]
        # "illegal": true ise şifre sor
        if a.get("illegal", False):
            if not illegal_sifre_kontrol():
                return Fore.RED + "Bu araca erişim için şifre doğrulanamadı."
        return (f"{Style.BRIGHT}{Fore.MAGENTA}Araç: {kelime}\n"
                f"{Fore.WHITE}Açıklama: {a.get('aciklama', 'Açıklama bulunamadı.')}\n"
                f"{Fore.LIGHTBLACK_EX}Örnek Kod:\n{a.get('ornek', 'Örnek kod bulunamadı.')}")
    else:
        return Fore.YELLOW + "Üzgünüm dostum, bunu bilmiyorum."

# Kullanıcı metnini yorumlama ve uygun yanıtı üretme
def yorumla_ve_uret(metin):
    """Kullanıcı girdisini yorumlar ve botun yanıtını döndürür."""
    metin = metin.lower().strip()

    # Genel karşılama ve vedalaşma yanıtları
    if "merhaba" in metin or "selam" in metin or "selamünaleyküm" in metin:
        return "Merhaba dostum! Sana nasıl yardımcı olabilirim?"
    if "nasılsın" in metin or "durumun nasıl" in metin:
        return "Ben bir yapay zekayım, bu yüzden 'iyiyim' diyebilirim. Sen nasılsın?"
    if "teşekkür ederim" in metin or "sağ ol" in metin or "teşekkürler" in metin:
        return "Rica ederim, ne demek! Başka bir sorun olursa buradayım."
    if "exit" in metin or "kapat" in metin or "güle güle" in metin:
        return "Görüşürüz dostum, kendine iyi bak!" # Bu mesaj main döngüsündeki "çık" ile çakışabilir, ayarlanmalı

    # Genel sorulara ve yorumlara botun "kendi fikirleri" gibi yanıtlar
    if "hava nasıl" in metin or "bugün hava" in metin:
        return "Ben bir yapay zekayım, dışarıdaki havayı bilemiyorum ama umarım güzel bir gündür!"
    if "neden buradasın" in metin or "amacı ne" in metin:
        return "Benim amacım sana Python programlama ve araçlar hakkında bilgi vermek, sana yardımcı olmak."
    if "en sevdiğin renk ne" in metin:
        return "Benim bir rengim yok, ama bilgiyi mavi ve yeşilin tonlarında görmekten hoşlanırım."
    if "yapay zeka nedir" in metin or "ai nedir" in metin:
        return "Yapay zeka, makinelerin insan benzeri zeka göstermesini sağlayan bir bilgisayar bilimi dalıdır. Öğrenme, problem çözme ve karar verme gibi yetenekleri kapsar."
    if "seni kim yaptı" in metin or "kurucun kim" in metin:
        return "Ben bir yapay zeka modeliyim ve Google tarafından eğitildim."
    if "komik bir şey söyle" in metin:
        return "Python programcıları neden gözlük takar? Çünkü daha iyi **py-thons** görebilmek için!"
    if "liste komutları" in metin or "liste metodları" in metin:
        return (f"{Fore.YELLOW}Liste işlemleri için 'append', 'extend', 'insert', 'remove', 'pop', 'clear', 'sort', 'reverse' gibi komutları sorabilirsin."
                f"\nÖrneğin: 'append kodu ver' veya 'liste sıralama nasıl yapılır?'")


    # JSON dosyalarındaki anahtar kelimeleri daha akıllıca kontrol et
    # Kullanıcının metni içinde geçen herhangi bir komut/araç adını bulmaya çalış
    # Uzun isimleri önce kontrol etmek, kısa olanların içinde kalmalarını engeller (örn: 'ip_tracer' önce, 'ip' sonra)
    tum_anahtarlar = sorted(list(python_araclari.keys()) + list(python_komutlari.keys()), key=len, reverse=True)

    for anahtar in tum_anahtarlar:
        if anahtar in metin:
            return kod_bilgisi_ver(anahtar)

    # Özel tanımlı menü örneği (istenirse tutulabilir veya kaldırılabilir)
    if "menü" in metin or "menu" in metin:
        return (
            f"{Fore.BLUE}Basit Python menü örneği:\n\n"
            f"{Fore.LIGHTBLACK_EX}def menu():\n"
            f"    while True:\n"
            f"        print('1. Seçenek 1')\n"
            f"        print('2. Seçenek 2')\n"
            f"        print('3. Çıkış')\n"
            f"        secim = input('Seçiminiz: ')\n"
            f"        if secim == '3':\n"
            f"            print('Çıkılıyor...')\n"
            f"            break\n"
            f"        else:\n"
            f"            print(f'Seçilen: {{secim}}')\n\n"
            f"menu()"
        )

    # Botun anlayamadığı durumlar
    return Fore.YELLOW + "Dostum bunu tam anlayamadım, biraz daha açık yazabilir misin?"

# Ana fonksiyon
def main():
    """Botun ana çalışma döngüsü."""
    print(Fore.CYAN + Style.BRIGHT + "🤖 Gelişmiş Python Kod Botu'na Hoş Geldin! (Çıkmak için 'çık' yaz.)\n")

    # Botu başlatmadan önce şifre kontrolü
    if not sifre_kontrol():
        return

    while True:
        soru = input(Fore.BLUE + "Sen: ").strip().lower()

        # Botu kapatma komutu
        if soru == "çık":
            print(Fore.RED + "Görüşürüz dostum, kendine iyi bak!")
            break

        # Yeni bilgi öğretme komutu
        if soru.startswith("öğret "):
            try:
                # "öğret kategori komut || açıklama || örnek_kod" formatını bekliyoruz
                parts = soru.split("||", 1) # Sadece ilk '||' ayracına göre böleriz
                if len(parts) < 2:
                    raise ValueError("Açıklama ve örnek '||' ile ayrılmalı.")

                komut_bilgisi_part = parts[0].strip()
                aciklama_ornek_part = parts[1].strip()

                # 'öğret kategori komut' kısmını ayır
                komut_bilgisi_parts = komut_bilgisi_part.split(" ", 2)
                if len(komut_bilgisi_parts) < 3:
                    raise ValueError("Komut formatı hatalı. 'öğret kategori komut' şeklinde olmalı.")

                kategori = komut_bilgisi_parts[1].lower()
                komut_adi = komut_bilgisi_parts[2].lower()

                # aciklama_ornek_part'ı açıklama ve örnek olarak ayır
                aciklama_ve_ornek = aciklama_ornek_part.split("||", 1)
                aciklama = aciklama_ve_ornek[0].strip()
                ornek = aciklama_ve_ornek[1].strip() if len(aciklama_ve_ornek) > 1 else "Örnek kod verilmedi."

                if not komut_adi or not aciklama:
                     raise ValueError("Komut adı veya açıklama boş olamaz.")

                if kategori == "python":
                    python_komutlari[komut_adi] = {"aciklama": aciklama, "ornek": ornek, "kategori": "öğretilen"}
                    json_kaydet("py_kodları.json", python_komutlari)
                    print(Fore.GREEN + f"'{komut_adi}' Python komutu olarak eklendi.")
                elif kategori in ("araç", "arac"):
                    # Öğretilen araçlara varsayılan olarak illegal=False ekliyoruz.
                    # Eğer illegal bir araç olarak öğretilmesini istiyorsan, komuta ek bir parametre gerekebilir.
                    python_araclari[komut_adi] = {"aciklama": aciklama, "ornek": ornek, "illegal": False}
                    json_kaydet("py_araçları.json", python_araclari)
                    print(Fore.GREEN + f"'{komut_adi}' araç olarak eklendi.")
                else:
                    print(Fore.RED + "Geçersiz kategori. 'python' veya 'araç' kullan.")
            except ValueError as ve:
                print(Fore.RED + f"Öğretme formatı hatalı: {ve}\nÖrnek:\n{Style.DIM}öğret python input || kullanıcıdan veri alır. || isim = input('Adın ne? '){Style.RESET_ALL}")
            except Exception as e:
                print(Fore.RED + f"Öğretme sırasında beklenmeyen bir hata oluştu: {e}")
            continue # Öğretme işleminden sonra ana döngüye devam et

        # Kullanıcı girdisini yorumla ve yanıtı al
        cevap = yorumla_ve_uret(soru)
        print(Fore.GREEN + "Bot:\n" + cevap)

# Ana fonksiyonu çalıştır
if __name__ == "__main__":
    main()
