import random

myslovar={
'vesh':['йо', 'камон', 'бичез'],
'animals':['кошка','собака','какаду']
}
myzadachi={
'first':'нарисуй {animals}',
'second':'нарисуй {animals} с ногой',
'third':'нарисуй {animals} с ногой в кепке'
}
def newslovar(slovar,zadachi):

    superslovar={}
    for zadacha in zadachi:
        print (zadacha)
        print (zadachi[zadacha])
        fratha=zadachi[zadacha]
        for slovo in slovar:
            print(slovo)
            if '{'+slovo+'}' in fratha:
                print('слово подошло')
                gener=slovar[slovo][random.randint(0,2)]
                otvet=fratha.format(**{slovo:gener})
                break
        else:
            print('не подощло')
            otvet='poshel nah'
        superslovar[zadacha]=otvet
    return superslovar

otvetik=newslovar(myslovar,myzadachi)
print(otvetik)
