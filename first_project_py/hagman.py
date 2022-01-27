import random

lm=["vert","chercheur","mercure","corde","plomb","scalpel","tremblement","fibre","bleu","chemin","parcours",
"enterrement","chapelle"]


print("hangman v1")
valeur=random.choice(lm)
lmot=[char for char in valeur]
lv=len(valeur)
tenta=lv
le=[]
for i in range(lv):
    le.append("-")
print(f"essayer de deviner le mot de {lv} vous avez au moin {tenta} tentative")
print(*le)
while True:
    if le.count("-")==0 and lmot.count("-")==lv:
        print('jouyeur gagne')
        break
    else:
        h=input(f'tentative {tenta} ')
        if h in lmot :
            ind=lmot.index(h)
            le[ind] = h
            lmot[ind]="-"
            print(*le)
        else:
            tenta-=1
            print(*le)
    if tenta <=0:
        print("game over ta perdue")
        break

    
