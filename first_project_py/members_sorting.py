import traceback
def select_student(students, threshold):
    accepter=[]
    refuser=[]
    d1=dict()
    for i in range(len(students)):
        if students [i][1] > threshold:
            accepter.append(students[i])
        else:
            refuser.append(students[i])
    d1["Accepted"]=sorted(accepter,key= lambda x: x[1],reverse=True)
    d1["Refused"]=sorted(refuser,key= lambda x: x[1])
    return  d1  

if __name__ == "__main__":

    assert select_student(
        [
            ["Kermit Wade", 27],
            ["Hattie Schleusner", 67],
            ["Ben Ball", 5],
            ["William Lee", 2],
        ],
        20,
    ) == {
        "Accepted": [["Hattie Schleusner", 67], ["Kermit Wade", 27]],
        "Refused": [["William Lee", 2], ["Ben Ball", 5]],
    }

    assert select_student(
        [
            ["Kermit Wade", 27],
            ["Hattie Schleusner", 67],
            ["Ben Ball", 5],
            ["William Lee", 2],
        ],
        50,
    ) == {
        "Accepted": [["Hattie Schleusner", 67]],
        "Refused": [["William Lee", 2], ["Ben Ball", 5], ["Kermit Wade", 27]],
    }

   