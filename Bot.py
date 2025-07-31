import json

def komut_al():
    return input("Komut: ").lower().strip()

# JSON'dan araçları yükle
try:
    with open("py_araclar.json", "r", encoding="utf-8") as f:
        araclar = json.load(f)
except FileNotFoundError:
    print("❌ py_araclar.json bulunamadı!")
    exit()

print("🔧 Python Komut Botu başlatıldı.")
print("Komutlar: " + ", ".join(araclar.keys()))
print("Çıkmak için: çık")

while True:
    komut = komut_al()

    if komut == "çık":
        print("Bot kapatılıyor...")
        break

    if komut in araclar:
        print(f"\n🛠 {komut.upper()} ➤ {araclar[komut]['aciklama']}\n")
        try:
            exec(araclar[komut]["ornek"])
        except Exception as e:
            print(f"❌ Kod çalıştırılırken hata oluştu: {e}")
    else:
        print("❗ Geçersiz komut. Lütfen listedeki komutlardan birini gir.")
