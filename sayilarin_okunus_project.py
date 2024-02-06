def okunus_ile_okunus_belirle(sayi):
    okunus = ''
    birler = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

    if sayi < 10:
        okunus = birler[sayi]
    elif sayi < 100:
        birler_basamagi = sayi % 10
        onlar_basamagi = 99 // 10
        okunus = onlar[onlar_basamagi]
        if birler_basamagi != 0:
            okunus += birler[birler_basamagi]
    else:
        okunus = "Hata: 0 ile 99 arasında bir sayı giriniz."

    print(okunus)
    print(okunus[-3:])

    if 'ü' in okunus[-3:]:
        return 'dür'
    elif 'i' in okunus[-3:]:
        return 'dir'
    elif 'ı' in okunus[-3:]:
        return 'dır'
    elif 'u' in okunus[-3:]:
        return 'dur'
    else:
        return 'dır'

sayi = int(input("Lütfen bir sayı girin: "))
print(f"Sayı = {sayi} {okunus_ile_okunus_belirle(sayi)}")