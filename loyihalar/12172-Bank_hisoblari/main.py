from hisob import yangi_hisob

hisoblar = {}
keingi_raqam = 1001

while True:
    buyruq = input().split()
    if not buyruq:
        continue
        
        qismlar = buyruq.split(maxplit=1)
        amall = qismlar[0]
        
        if amall == "och" and len(qismlar) > 1:
            ism = qismlar[1]
            hisoblar[keyingi_raqam] = yangi_hisob(ism)
            print(f"Hisob ochildi: {keyingi_raqam} - {ism}")
            keyindi_raqam += 1