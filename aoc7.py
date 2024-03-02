import pandas as pd
aryan = pd.read_csv('day7.txt')
hands = list(aryan.iloc[:]['Hand'])
# print(sorted(hands[40]))
def typeHand(a):
    count1=0
    count2=0
    count3=0
    count4=0
    count0 = a[0]
    if a[1]!=a[0]:
        count1 = a[1]
    if a[2]!=a[0] and a[2]!=a[1]:
        count2 = a[2]
    if a[3]!=a[0] and a[3]!=a[1] and a[3]!=a[2]:
        count3 = a[3]
    if a[4]!=a[0] and a[4]!=a[1] and a[4]!=a[2] and a[4]!=a[3]:
        count4 = a[4]
    return 
typeHand(hands[0])
# def compare(a,b):






