import json
import getpass

def verileri_yukle():
    try:
        with open("sadik_bot.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def verileri_kaydet(beyin):
    with open("sadik_bot.json", "w") as f:
        json.dump(beyin, f, indent=4, ensure_ascii=False)

def kullanici_dogrula():
    # Örnek kullanıcı adı ve şifre (bunu istersen değiştirebilirsin)
    dogru_kullanici = "demir"
    dogru_sifre = "GizliSifre123"

    print("Kullanıcı adı ve şifre ile giriş yapın.")
    kullanici = input("Kullanıcı adı: ")
    sifre = getpass.getpass("Şifre: ")

    if kullanici == dogru_kullanici and sifre == dogru_sifre:
        print("Giriş başarılı. Yapay zekaya hoş geldin!")
        return True
    else:
        print("Hatalı kullanıcı adı veya şifre.")
        return False

def sadik_chatbot():
    if not kullanici_dogrula():
        return

    beyin = verileri_yukle()
    print("\n🤖 Sadık Yapay Zeka hazır. (Çıkmak için 'çık' yaz.)")
    
    while True:
        soru = input("Sen: ").strip().lower()
        if soru == "çık":
            print("Görüşürüz!")
            break

        if soru in beyin:
            print("Bot:", beyin[soru])
        else:
            cevap = input("Bu soruya ne cevap vermemi istersin?: ")
            beyin[soru] = cevap
            verileri_kaydet(beyin)
            print("✅ Öğrendim!")

if __name__ == "__main__":
    sadik_chatbot()
