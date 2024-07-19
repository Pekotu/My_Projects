import piskvorky_funkce as pf

#nova hra
while True:
    cil=0
    sirka, vyska, papir = pf.zadej_velikost_papiru()

    pf.zadej_pocet_vyteznych_znaku()

    znacka = ''
    hrac=''
    result = ''

    #hraci smycka
    while True:
        if hrac == 'Hrac 1':
            hrac = 'Hrac 2'
            znacka = 'O'
        else:
            hrac = 'Hrac 1' 
            znacka = 'X'

        pf.vypis_papiru(sirka, papir)
        pf.zapis_znacky(hrac, sirka, vyska, znacka, papir)
        
        result=pf.kontrola_vytezstvi(papir, sirka, vyska)
        
        text = ''
        if result == "X":
            text = 'Vyhral Hrac 1 s X'
        elif result == "O": 
            text  ='Vyhral Hrac 2 s O'

        if result in ['X', 'O']:
            print()
            print()
            print()
            print('----------------------------------------')
            print('---------- ', text ,' -----------  ')
            print('----------------------------------------')
            print()
            pf.vypis_papiru(sirka, papir)
            print()
            break
   
    if not pf.pokracovat_ve_hre():
        break

print('konec programu')


    





# papir= [
# ['X', 'O', '_', 'O', '_'], 
# ['X', 'X', '_', 'O', '_'], 
# ['O', 'O', 'X', 'X', '_'], 
# ['_', 'X', '_', 'O', 'X'], 
# ['X', '_', 'O', '_', '_']
# ]

#pf.vypis_papiru(5, papir)

#vysledek = pf.kontrola_vytezstvi(papir, 5, 5)
#print(vysledek)