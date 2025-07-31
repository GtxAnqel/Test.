import json

def komut_al():
    return input("Komut: ").lower().strip()

# JSON dosyasını oku
with open("py_araclar.json", "r", encoding="utf-8") as f:
    araclar = json.load(f)

print("Bot başlatıldı. Komut gir (örn: keylogger, ip_tracer):")

while True:
    komut = komut_al()
    
    if komut == "çık":
        print("Bot kapatılıyor...")
        break

    if komut in araclar:
        print(f"{komut} çalıştırılıyor...")
        print("Kod yürütülüyor. Lütfen bekleyin...\n")
        try:
            exec(araclar[komut]["ornek"])
        except Exception as e:
            print(f"Hata oluştu: {e}")
    else:
        print("Bilinmeyen komut. Lütfen geçerli bir araç adı gir.")
