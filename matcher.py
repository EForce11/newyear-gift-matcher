import random

def oku_isimler(dosya_adi):
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as dosya:
            isimler = [satir.strip() for satir in dosya.readlines() if satir.strip()]
        return isimler
    except FileNotFoundError:
        print(f"'{dosya_adi}' dosyası bulunamadı. Lütfen dosyanın mevcut olduğundan emin olun.")
        return []

def eslestir_isimler(isimler):
    random.shuffle(isimler)
    eslesmeler = list(zip(isimler, isimler[1:] + [isimler[0]]))
    return eslesmeler

def main():
    dosya_adi = "isimler.txt"
    isimler = oku_isimler(dosya_adi)

    if len(isimler) < 4:
        print("Lütfen 'isimler.txt' dosyasına en az 4 isim ekleyin.")
        return

    eslesmeler = eslestir_isimler(isimler)

    print("\nEşleştirmeler:")
    for e in eslesmeler:
        print(f"{e[0]} -> {e[1]}")

if __name__ == "__main__":
    main()
