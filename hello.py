

#принимает мужика и вывдоит его данные
def printman(man):
    print('привет',man['name'])
    print ('возраст',man['age'])
#принимает и выводит мужиков
def vivod(dudes):
    counter=0
    for dude in dudes:
        counter=counter+1
        print('мужик №',counter)
        printman(dude)

#создает мужика и возвращает
def mansaver():
    pop=input('name')
    a=input('age')
    d={'name':pop,'age':a}

    return d

def superp():
    myziki=[]
    chisla=[0,0,0,0,0]
    for chislo in chisla:
        dude=mansaver()
        myziki.append(dude)#добавляет мужика в массив мужиков
    vivod(dudes=myziki)




superp()
