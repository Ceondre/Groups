
import csv
import random

anzahl_gruppenmitglieder=0
anzahl_gruppen=0

list_all = []
def get_persons(file):
    global list_all
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            list_all.append(row)
        csv_file.close()
    return list_all



def groups(anzahl_gruppenmitglieder= None, anzahl_gruppen=None, list_all=None): # anzahl_gruppenmitglieder und anzahl_gruppen müssen gerade sein
    if anzahl_gruppenmitglieder is None:
        anzahl_gruppenmitglieder = [round(len(list_all) / anzahl_gruppen), len(list_all) % anzahl_gruppen ]
        anzahl_gruppen= [anzahl_gruppen, 0]

    elif anzahl_gruppen is None:
        anzahl_gruppen =[ round(len(list_all)/anzahl_gruppenmitglieder), len(list_all)%anzahl_gruppenmitglieder]
        anzahl_gruppenmitglieder=[anzahl_gruppenmitglieder, 0]
    elif anzahl_gruppen is None and anzahl_gruppenmitglieder is not None:
        anzahl_gruppen = [anzahl_gruppen,0]
        anzahl_gruppenmitglieder = [anzahl_gruppenmitglieder,0]
    else:
        print("Error")


    return anzahl_gruppenmitglieder, anzahl_gruppen


def make_groups(anzahl_gruppen, anzahl_gruppenmitglieder,list_all):
    extra = anzahl_gruppen[1] + anzahl_gruppenmitglieder[1]
    anzahl_gruppen = anzahl_gruppen[0]
    anzahl_gruppenmitglieder= anzahl_gruppenmitglieder[0]
    Gruppen= {}
    liste_besetzt= []
    liste_a = []
    for o in range(anzahl_gruppen):
        for i in range(anzahl_gruppenmitglieder):
            test = False
            while not test:
                a = random.choice(list_all)
                if a not in liste_besetzt:
                    liste_a.append(a)
                    liste_besetzt.append(a)
                    test = True
        if extra != 0:
            test = False
            while not test:
                a = random.choice(list_all)
                if a not in liste_besetzt:
                    liste_a.append(a)
                    liste_besetzt.append(a)
                    extra = extra -1
                    test = True

        Gruppen[o]=liste_a
        liste_a = []
    print(Gruppen)
    return Gruppen

def add_Person(Person_name, destination_group):
    group[destination_group].append(Person_name)
def remove_Person(Person_name, destination_group):
    group[destination_group].remove(Person_name)
def switch(Person1_name, Person2_name, Person1_group, Person2_group):
    add_Person(Person1_name, Person2_group)
    add_Person(Person2_name, Person1_group)
    remove_Person(Person1_name, Person1_group)
    remove_Person(Person2_name, Person2_group)





liste= get_persons("/home/clemens/Groups/hand.csv")[0]
print(liste)
x = 2 #anzahl gruppenmitglieder
b = None #anzahl Gruppen
print("liste Gruppenmitglieder: ",groups(list_all= liste, anzahl_gruppenmitglieder= x, anzahl_gruppen= b)[0])
print("anzahl Gruppen: ", groups(list_all=liste, anzahl_gruppenmitglieder=x, anzahl_gruppen= b)[1])
group = make_groups(anzahl_gruppen= (groups(list_all= liste, anzahl_gruppenmitglieder= x, anzahl_gruppen= b)[1]), anzahl_gruppenmitglieder = (groups(list_all=liste, anzahl_gruppenmitglieder=x, anzahl_gruppen= b)[0]), list_all= liste)
add_Person(Person_name="ME",destination_group= 1)
print(group)
add_Person(Person_name="you", destination_group= 0)
print(group)
switch(Person1_name= "you", Person2_name = "ME", Person1_group = 0, Person2_group=1)
print(group)
