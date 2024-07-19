def test_zadane_hodnoty_papiru(hodnota):
    try:
        hodnota = int(hodnota)
        if hodnota > 0:
            return hodnota
        else:
            return False
        
    except ValueError:
        return False

#--------------------------------------

def test_zadane_hodnoty_znacky(hodnota):
    try:
        hodnota = int(hodnota)
        if hodnota >= 0:
            return hodnota
        else:
            return -1
        
    except ValueError:
        return -1

#--------------------------------------


def zadej_velikost_papiru():
    #zadani a test velikosti papiru
    while True:
        hodnota=input("Zadej sirku hraciho prostoru: ")
        
        sirka = test_zadane_hodnoty_papiru(hodnota)
        if sirka:
            break
        else:
            print('Zadaná hodnota musí být kladné číslo, zadej číslo znovu' + '\n')

    while True:
        hodnota=input("zadej vysku hraciho prostoru: ")
               
        vyska = test_zadane_hodnoty_papiru(hodnota)
        if vyska:
            break
        else:
            print('Zadaná hodnota musí být kladné číslo, zadej číslo znovu' + '\n')
    
    # vytvori prazdny papir 
    papir=[]
    for v in range(vyska):
        radek=[]
        radek = sirka*['_']
        papir.append(radek)
    return [sirka, vyska, papir]

#-----------------------------
def zadej_pocet_vyteznych_znaku():
    global cil
    
    while True:
        print()
        hodnota = input('Zadej na kolik vyteznych znaku hrajete: ')
        print()

        cil = test_zadane_hodnoty_papiru(hodnota)
        
        if cil:
            return
            
        else:
            print('Zadana hodnota musi byt plusove cislo, zkus to znovu')



#-----------------------------
def vypis_papiru(sirka, papir):
    #tisk cisel sloupcu
    to_print1='   '
    to_print2='   '

    to_print1+= ('X'+' ')*sirka 
    print(to_print1)

    for s in range(sirka):
        to_print2+= str(s)+' ' 
    
    print(to_print2)

    #tisk obsahu radku
    for r, row in enumerate(papir):
        to_print3= 'Y'+str(r)+' '
        for s in row:
            to_print3 += str(s)+' ' 
        print(to_print3)
    print()
    

#--------------------------------
def zapis_znacky(hrac, sirka, vyska, znacka, papir):
    #hrač zada souradnice kam chce umistit svou znacku
    
    
    while True:
        while True:
            hodnota = input(f"{hrac} zadej X souradnici pro svou novou znacku :")
            x= test_zadane_hodnoty_znacky(hodnota)
            if 0 <= x < sirka:
                break
            else:
                print(f'Zadaná hodnota musí být kladné číslo v rozmezi 0 až {sirka-1}, zadej číslo znovu' + '\n')
                
        while True:
            hodnota = input(f"{hrac} zadej Y souradnici pro svou novou znacku:")
            y=test_zadane_hodnoty_znacky(hodnota)
            if 0 <= y < vyska:
                break
            else:
                print(f'Zadaná hodnota musí být kladné číslo v rozmezi 0 až {vyska-1}, zadej číslo znovu' + '\n')
        
        if kontrola_obsazeni_pozice(x, y, papir):
            break
        else:
            print("Na zadanych souradnicich je již znacka. Zkus to znovu." + '\n')
    
    papir[y][x]=znacka

#-------------------------------------
def kontrola_obsazeni_pozice(x,y,papir):
    if papir[y][x]!="_":
        return False
    else:
        return True

#---------------------------------------
def kontrola_vytezstvi(papir, sirka, vyska):
    
    #cil=5   
    
    #radky
    for radek in papir:
        pocet_x= 0
        pocet_o= 0

        for hodnota in radek:
            
            if hodnota=="X": 
                pocet_x+=1
                if pocet_x==cil:
                    return 'X' #vitezstvi
            else:
                pocet_x=0
            
            if hodnota=="O": 
                pocet_o+=1
                if pocet_o==cil:
                    return 'O' #vitezstvi
            else:
                pocet_o=0
    
           
    #sloupce
    for sloupec in range(sirka):
        pocet_x= 0
        pocet_o= 0

        for radek in range(vyska):
            #print(f'{radek=}')
            #print(f'{sloupec=}')
            #print(f'{papir[radek][sloupec]=}')
            
            if papir[radek][sloupec]=="X": 
                pocet_x+=1
                if pocet_x==cil:
                    return 'X' #vitezstvi
            else:
                pocet_x=0

            if papir[radek][sloupec]=="O": 
                pocet_o+=1
                if pocet_o==cil:
                    return 'O' #vitezstvi
            else:
                pocet_o=0
    

    #diagonala \
    
    for diag in range(sirka):
        pocet_x= 0
        pocet_o= 0
        for v in range(vyska):
           
            radek = v
            sloupec = v+diag
            if sloupec >= sirka:
                continue

            hodnota= papir[radek][sloupec]    
            # print(f'{radek=}')
            # print(f'{sloupec=}')
            # print(f'{hodnota=}')
            
            if hodnota=="X": 
                pocet_x+=1
                if pocet_x==cil:
                    return 'X' #vitezstvi
            else:
                pocet_x=0
            
            if hodnota=="O": 
                pocet_o+=1
                if pocet_o==cil:
                    return 'O' #vitezstvi
            else:
                pocet_o=0

     #diagonala /
    
    for diag in range(1,vyska):
        pocet_x= 0
        pocet_o= 0
        for r in range(sirka):
            
            radek = r + diag
            sloupec = r
            if radek >= vyska:
                continue

            hodnota= papir[radek][sloupec]    
            #print(f'{radek=}')
            #print(f'{sloupec=}')
            #print(f'{hodnota=}')
            
            if hodnota=="X": 
                pocet_x+=1
                if pocet_x==cil:
                    return 'X' #vitezstvi
            else:
                pocet_x=0
            
            if hodnota=="O": 
                pocet_o+=1
                if pocet_o==cil:
                    return 'O' #vitezstvi
            else:
                pocet_o=0

    return '-'


#-------------------------------------
def pokracovat_ve_hre():
    while True:
        hodnota = input('Chcete hrat znovu? (A/N): ')

        if hodnota == 'a' or hodnota == 'A':
            return True
        
        elif hodnota == 'n' or hodnota == 'N':
            return False
        
        else:
            print('Odpovězte A pro pokračovat nebo N pro konec.' )
        