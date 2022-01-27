

def diplay_matrice():
    """afficher le terain de jeux"""
    print(" . | . | . "," . | . | . "," . | . | . ",sep='\n')


def win(list, ele):
    """verifier au cas au il ya un gagnant"""
    lose=0
    win=1
    win_1 = list[0]== ele and list[1]== ele and list[2]== ele
    win_2=list[3]== ele and list[4]== ele and list[5]== ele
    win_3=list[6]== ele and list[7]== ele and list[8]== ele
    win_4=list[0]== ele and list[3]== ele and list[6]== ele
    win_5=list[1]== ele and list[4]== ele and list[7]== ele
    win_6=list[2]== ele and list[5]== ele and list[8]== ele
    win_8=list[0]== ele and list[4]== ele and list[8]== ele
    win_9=list[2]== ele and list[4]== ele and list[6]== ele
    
    if win_1 or win_2 or win_3 or win_4 or win_5 or win_6 or win_8 or win_9  :
        return win
    else :
        return lose




          
