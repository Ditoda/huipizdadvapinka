def vivod(films):
    print('Йоу',films['название'])

def kinchiki():
    name=input('название')
    rate=input('оценка')
    dicti={'название':name,'оценка':rate}

    return dicti
def massiv():
    films=[]
    kolvo=[0,0,0,0,0]
    for chislo in kolvo:
        film=kinchiki()
        films.append(film)
    vivod(films=film)
massiv()
