import tic_tac_toe_fucn
#j1 'O'
#j2 'X'
p={
    'j1':{
        'name':'','signe':'O'
    },
    'j2':{
        'name':'','signe':'X'
    }
}
l = ["."]*9
p['j1']['name']=input("donner le nom du joueur 1 :")
p['j2']['name']=input("donner le nom du joueur 2 :")
print( '> > > ' + p['j1']['signe'] + ' associer a ' + p['j1']['name'])
print( '> > > ' + p['j2']['signe'] + ' associer a ' + p['j2']['name'])
print("joue commencer:...")
tic_tac_toe_fucn.diplay_matrice()
tour=0
while True:
    if tour==0:
        jtour = p['j1']['signe']
        jname = p['j1']['name']
        tour += 1
    else:
        jtour = p['j2']['signe']
        jname = p['j2']['name']
        tour -= 1
    move=int(input(  f' {jname} choisisser 1-9 deffinissant votre pas :' ))
    l[move-1]=jtour
    action=tic_tac_toe_fucn.win(l,jtour)
    print ( f' {l[0]} | {l[1]} | {l[2]} \n {l[3]} | {l[4]} | {l[5]} \n {l[6]} | {l[7]} | {l[8]} ')
    cout_xo=int(l.count("X")+l.count("O"))
    if cout_xo < 9:
        if action == 1:
            print(f' {jname} wins')
            break 
        else:
            continue
    else:
        print("game over")
        break   