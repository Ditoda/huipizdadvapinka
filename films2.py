massiv=[]
def printlist():
    print(massiv)
def kinoinput():
    massiv.append(createkino())

def createkino():
    kino=input('name')
    rate=input('rate')
    looking=input('true or false')
    film={
    'name':kino,
    'rate':rate,
    'look':looking
    }
    return film
def kinoinput():
    massiv.append(createkino())
def vvod():
    print('список или добавить?')
    otvet=input('ответ')
    if otvet=='список':
        printlist()
    elif otvet==('добавить'):
        kinoinput()
    elif otvet=='exit':
        exit()
    else:
        print('нахуй иди')
    vvod()
vvod()
