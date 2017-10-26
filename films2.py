
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

massiv=[]
for i in range(0,5):
    massiv.append(createkino())
    print(massiv)
    print('===')
