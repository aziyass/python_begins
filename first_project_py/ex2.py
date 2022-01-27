import string  

def conter_mot(line_given):
    line=line_given.lower()
    line_1=line.translate(line.maketrans('','',string.punctuation))
    line_2=line_1.split()
    mot_f=[]
    d1=dict()
    for i in line_2:
        if i not in mot_f:
            mot=i
            val=0
            for j in line_2:
                if mot == j :
                    val+=1
                    mot_f.append(mot)
            d1.update({f'{mot}' : f'{val}'})
    print(d1)       

phrase=input("phrase :")
print(conter_mot(phrase))
