emeklimaas = 10000
durum = True

def parayatır(add):
    addtutar = int(input("Yatırmak istediğiniz tutarı giriniz: "))
    if addtutar > 5:
        add += addtutar
        print(f"Paranız hesabınıza yatırıldı. Mevcut bakiyeniz: {add} TL.")
    elif addtutar == 5:
        print("Lütfen 5 TL'den yüksek tutar yatırın.")

    global durum
    sonsorgu = input("Çıkış yapmak istiyor musunuz? (E/H): ").strip().lower()
    if sonsorgu == "e":
        print("Uygulamadan çıkış yapılıyor...")
        durum = False
    elif sonsorgu == "h":
        print("Ana menüye dönülüyor...")

def paraçekme(çekme):
    cıkar = int(input("Çekeceğiniz tutarı giriniz: "))
    if cıkar > 5:
        çekme -= cıkar
        print(f"Çekeceğiniz tutar {cıkar} TL. Kalan bakiyeniz {çekme} TL.")
    elif cıkar == 5:
        print("5 TL maalesef çekilememektedir.")
    global durum
    sonsorgu = input("Çıkış yapmak istiyor musunuz? (E/H): ").strip().lower()
    if sonsorgu == "e":
        print("Uygulamadan çıkış yapılıyor...")
        durum = False
    elif sonsorgu == "h":
        print("Ana menüye dönülüyor...")

def bakiyesorgula(bakiye):
    print(f"Güncel Bakiyeniz: {bakiye} TL.")
    global durum
    sonsorgu = input("Çıkış yapmak istiyor musunuz? (E/H): ").strip().lower()
    if sonsorgu == "e":
        print("Uygulamadan çıkış yapılıyor...")
        durum = False
    elif sonsorgu == "h":
        print("Ana menüye dönülüyor...")

def çıkış():
    global durum
    sonsorgu = input("Çıkış yapmak istiyor musunuz? (E/H): ").strip().lower()
    if sonsorgu == "e":
        print("Uygulamadan çıkış yapılıyor...")
        durum = False
    elif sonsorgu == "h":
        print("Ana menüye dönülüyor...")


while durum == True:
    print("Bankamatik Uygulaması \n")
    print("1- Para Yatırma İşlemi")
    print("2- Para Çekme İşlemi")
    print("3- Bakiye Sorgulama İşlemi")
    print("4- Çıkış")
    secim = int(input("Hangi işlemi yapmak istiyorsunuz? (1/2/3/4): "))

    if secim == 1:
        parayatır(emeklimaas)
    elif secim == 2:
        paraçekme(emeklimaas)
    elif secim == 3:
        bakiyesorgula(emeklimaas)
    elif secim == 4:
        çıkış()
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")

print("Uygulama sonlanmıştır.")
